from typing import TYPE_CHECKING, Any, Dict, Type, Union, Optional, Sequence
from pathlib import Path
from multiprocessing import Pool

import attr
import open3d as o3d
import psutil
from loguru import logger
from pydantic import BaseModel, validator, parse_file_as
from codetiming import Timer

from threedframe import utils
from threedframe.models import ModelData, ModelVertex
from threedframe.constant import RenderFileType
from threedframe.scad.joint import Joint

from ..config import config

if TYPE_CHECKING:
    from .interfaces import CoreMeta, JointMeta, LabelMeta, FixtureMeta


class JointDirectorParams(BaseModel):
    joint_builder: Optional[Type["JointMeta"]] = Joint
    fixture_builder: Optional[Type["FixtureMeta"]] = None
    fixture_label_builder: Optional[Type["LabelMeta"]] = None
    core_builder: Optional[Type["CoreMeta"]] = None
    core_label_builder: Optional[Type["LabelMeta"]] = None

    vertices: Optional[Sequence[Union[int, str]]] = None
    render: bool = False
    render_file_type: Optional[RenderFileType] = RenderFileType.STL
    model: Union[Path, "ModelData"]
    overwrite: bool = False

    @staticmethod
    def _resolve_edge_relations(
        model: "ModelData", vertices: Dict[int, "ModelVertex"]
    ) -> "ModelData":
        _vertices = {}
        for vidx, vertex in vertices.items():
            edges = []
            for edge in vertex.edges:
                if vidx == edge.joint_vidx:
                    target = model.get_edge_target_vertex(edge)
                    logger.info(
                        "mapped vertex[{}] -> edge[{}] -> vertex[{}]", vidx, edge.eidx, target.vidx
                    )
                    edges.append(edge.copy(update=dict(joint_vertex=vertex, target_vertex=target)))
            _vertices[vidx] = vertex.copy(update=dict(edges=edges))
        return model.copy(update=dict(vertices=_vertices))

    @validator("model", always=True)
    def validate_model_data(cls, v: Union[Path, "ModelData"], values: Dict[str, Any]) -> ModelData:
        if isinstance(v, Path):
            v: ModelData = parse_file_as(ModelData, v)
        verts = values["vertices"]
        resolve_verts = v.vertices
        if verts is not None:
            _verts = []
            for vl in verts:
                if not str(vl).isnumeric():
                    _verts.append(v.get_vidx_by_label(vl))
                else:
                    _verts.append(int(vl))
            # scoped vertices down to requested by params.
            resolve_verts = {k: v for k, v in v.vertices.items() if k in _verts}
        v = cls._resolve_edge_relations(v, resolve_verts)
        return v


@attr.s(auto_attribs=True)
class JointDirector:
    params: JointDirectorParams
    joints: Dict["ModelVertex", "JointMeta"] = attr.ib(factory=dict)
    scad_paths: Dict["ModelVertex", Path] = attr.ib(factory=dict)
    render_paths: Dict["ModelVertex", Path] = attr.ib(factory=dict)

    @property
    def builder_params(self) -> Dict[str, Any]:
        _build_params = self.params.dict(
            exclude={"model", "vertices", "joint_builder", "render", "render_file_type"},
            exclude_none=True,
            exclude_unset=True,
        )
        return _build_params

    def vertex_by_idx_or_label(self, v: Union[int, str]) -> "ModelVertex":
        """Resolve vertex obj from vidx or label."""
        vidx = self.params.model.get_vidx_by_label(v)
        vidx = vidx if vidx is not None else int(vidx)
        return self.params.model.vertices[vidx]

    def create_joint(self, vertex: Union[int, "ModelVertex"]) -> "JointMeta":
        """Create joint object to be assembled."""
        vert = vertex if isinstance(vertex, ModelVertex) else self.params.model.vertices[vertex]
        return self.params.joint_builder(vertex=vert, **self.builder_params)

    @logger.catch(reraise=True)
    def build_joint(self, vertex: "ModelVertex") -> Optional["JointMeta"]:
        scad_path = self.get_joint_file_path(vertex.vidx)
        if not self.params.overwrite and scad_path.exists() and self.params.render:
            logger.warning(f"Joint for vertex: {vertex.vidx} already exists, skipping to render...")
            return self.render_joint(scad_path)
        logger.info("Building joint for vertex: {}", vertex.vidx)
        joint = self.create_joint(vertex=vertex)
        joint.assemble()
        self.write_joint(joint)
        return joint

    def get_joint_file_path(self, vertex_label: str) -> Path:
        file_name = f"joint-{vertex_label}.scad"
        out_path = config.RENDERS_DIR / file_name
        return out_path

    def write_joint(self, joint: "JointMeta"):
        out_path = self.get_joint_file_path(joint.vertex.label)
        utils.write_scad(joint.scad_object, out_path, header=config.scad_header)
        if self.params.render:
            self.render_joint(out_path)

    def render_joint(self, scad_path: Path):
        out_path = scad_path.with_suffix(f".{self.params.render_file_type}")
        logger.success("Writing mesh -> {}", out_path)
        proc = utils.openscad_cmd(
            *self.params.render_file_type.scad_args, "-o", str(out_path), str(scad_path)
        )
        for line in iter(proc.stderr.readline, b""):
            outline = line.decode().rstrip("\n")
            logger.debug("[OpenSCAD]: {}", outline)

    @Timer(logger=logger.success)
    def assemble(self):
        logger.info("Constructing joint objects for {} vertices.", len(self.params.model.vertices))
        logger.debug("Director builders: {}", self.builder_params)
        verts = self.params.model.vertices.values()
        for vert in verts:
            self.build_joint(vert)


class ParallelJointDirector(JointDirector):
    @Timer(logger=logger.success)
    def assemble(self):
        logger.info("Constructing joint objects for {} vertices.", len(self.params.model.vertices))
        logger.debug("Director builders: {}", self.builder_params)
        workers = psutil.cpu_count()
        verts = self.params.model.vertices.values()
        chunk_size = len(verts) // workers
        if len(verts) <= workers:
            chunk_size = 1
        logger.info("parallel chunk size: ({} // {}) = {}", len(verts), workers, chunk_size)
        with Pool(processes=workers) as pool:
            list(pool.imap_unordered(self.build_joint, verts, chunksize=chunk_size))
