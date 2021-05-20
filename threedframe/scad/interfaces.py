import abc
from typing import TYPE_CHECKING, Dict, List, Type, Tuple, Iterator, Optional

import attr
import solid as sp

from threedframe import utils

if TYPE_CHECKING:
    from .label import LabelParams
    from ..models import MeshData, ModelVertex
    from .fixture import FixtureParams


@attr.s(auto_attribs=True)
class ScadMeta(abc.ABC):
    scad_object: Optional[sp.OpenSCADObject] = None

    @abc.abstractmethod
    def assemble(self):
        raise NotImplementedError


@attr.s(auto_attribs=True)
class FixtureMeta(ScadMeta, abc.ABC):
    params: "FixtureParams" = ...

    @abc.abstractmethod
    def create_base(self) -> sp.OpenSCADObject:
        raise NotImplementedError

    @abc.abstractmethod
    def do_extrude(self, obj: sp.OpenSCADObject) -> sp.OpenSCADObject:
        raise NotImplementedError

    @abc.abstractmethod
    def do_transform(self, obj: sp.OpenSCADObject) -> sp.OpenSCADObject:
        raise NotImplementedError

    def assemble(self):
        obj = self.create_base()
        obj = self.do_extrude(obj)
        obj = self.do_transform(obj)
        self.scad_object = obj


@attr.s(auto_attribs=True)
class CoreMeta(ScadMeta, abc.ABC):
    fixtures: List["FixtureMeta"] = ...
    meshes: Dict[str, "MeshData"] = ...

    @abc.abstractmethod
    def create_hull_cubes(self):
        raise NotImplementedError

    def assemble(self):
        fixture_vertex_cubes = list(self.create_hull_cubes())
        obj = sp.hull()(*fixture_vertex_cubes)
        self.scad_object = obj

