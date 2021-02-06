# -*- coding: utf-8 -*-

"""3DFrame joint module."""

import json
import pickle
import shutil
import tempfile
from os import PathLike

import vg
import numpy as np
from rich import print, progress
from solid import *
from sympy import Float, Plane, Point
from solid.utils import *

from threedframe import utils
from threedframe.utils import ModelData, label_size

ROOT = Path(__file__).parent

MODEL_DATA_PATH = None
MODEL_DATA: Optional[ModelData] = None

LIB_DIR = ROOT / "lib"
MCAD = LIB_DIR / "MCAD"

TAU = 6.2831853071  # 2*PI
deg = lambda x: 360 * x / TAU

mcad = import_scad(str(Path(ROOT / "lib/MCAD")))
dotSCAD = import_scad(str(Path(ROOT / "lib/dotSCAD/src")))

MM = 1
INCH = 25.4 * MM

inch = lambda x: x * INCH

SEGMENTS = 48

CORE_SIZE = inch(1.4)

# Global Params
GAP = 0.02  # fudge factor

# Fixture Params
SUPPORT_SIZE = inch(0.69)  # size of wooden support
FIXTURE_WALL_THICKNESS = 6  # thickness of support fixture wall
FIXTURE_HOLE_SIZE = SUPPORT_SIZE + GAP
FIXTURE_SIZE = FIXTURE_HOLE_SIZE + FIXTURE_WALL_THICKNESS

FIXTURE_ANGLE_FUDGE = 6.3  # Fudge value for fixture angles length.


def assemble_core(
    vidx: int,
    fixture_points: List[Point3],
    debug=False,
    progress: Optional[progress.Progress] = None,
):
    union()
    prog = progress
    core_radius = CORE_SIZE / 2
    core = sphere(core_radius)

    # Here, we use the fixture reference points
    # to calculate a safe area (one that isn't covered by a fixture)
    # to place our vertex label.

    # reference sphere for calculations
    sphere_obj = Sphere(Point3(*ORIGIN), radius=CORE_SIZE)

    # Create a line segment from the fixture points
    # reaching back to origin.
    # Adds the point of contact of the line on the core to the array below.
    points_on_core = []
    for point in fixture_points:
        sphere_at_point = Sphere(point, FIXTURE_SIZE)
        line_to_origin_sphere: LineSegment3 = sphere_at_point.connect(sphere_obj)
        print(line_to_origin_sphere, line_to_origin_sphere.p2)
        points_on_core.append(line_to_origin_sphere.p2)

    # Determine mean/stdev for Guassian distribution.
    points_dataset = list(frange(-core_radius, core_radius))
    points_mean = statistics.mean(points_dataset)
    points_stdev = statistics.stdev(points_dataset)
    points_gauss = lambda: random.gauss(points_mean, points_stdev)

    # Generate "random" XYZ coords using Guassian distribution for uniformity
    # on the surface of the spherical core.
    attempted_points = []
    fixture_boundary = reversed(range(10, 21))
    current_boundary = next(fixture_boundary)
    task = None
    while True:
        ran_x = points_gauss()
        ran_y = points_gauss()
        ran_z = points_gauss()
        norm = 1 / math.sqrt(math.pow(ran_x, 2) + math.pow(ran_y, 2) + math.pow(ran_z, 2))
        ran_x *= norm
        ran_y *= norm
        ran_z *= norm
        # Subtract 4 to make the point 4mm inside the core,
        # so it will later extruded outwards with the correct orientation.
        ran_x *= core_radius - 4
        ran_y *= core_radius - 4
        ran_z *= core_radius - 4
        _point = (ran_x, ran_y, ran_z)
        ran_point = Point3(*_point)
        roun_point = utils.round_point(ran_point, n_digits=6)
        if roun_point in attempted_points:
            current_boundary = next(fixture_boundary)
            prog.print(f"[red bold]Reducing boundary to: {current_boundary}")
            attempted_points = []
            continue
        attempted_points.append(roun_point)
        if task is None:
            task = prog.add_task(
                f"  Computing Core Label Position for V{vidx}",
                ran_point=ran_point,
                current_boundary=current_boundary,
            )
        else:
            prog.update(task, ran_point=ran_point, current_boundary=current_boundary)
        # Create a sphere (with some breathing room) at each of
        # the previously collected points of fixture contact on the core.
        # Then, test to see if our random point does not intersect with any
        # of the spheres. This ensures our point is in a clear area on the core.
        is_clear_fixtures = [
            not ran_point.intersect(Sphere(p, FIXTURE_SIZE + current_boundary))
            for p in points_on_core
        ]
        prog.update(task, results=is_clear_fixtures)
        if all(is_clear_fixtures):
            label_point = ran_point
            prog.update(task, visible=False)
            break

    print(
        f"[bold white]Found clear point: [/]{label_point} @ {current_boundary}[bold white] boundary."
    )

    text_el, res_vals = label_size(
        f"V{vidx}\n ",
        halign="center",
        size=min([current_boundary, 8]),
        width=min([current_boundary, 16]),
        depth=4,
    )
    inverse_label = Point3(-label_point.x, -label_point.y, -label_point.z)
    text_el = transform_to_point(
        text_el.copy(), dest_point=label_point, dest_normal=inverse_label.normalized()
    )
    core -= text_el
    return core
def assemble_vertex(vidx: int, debug=False, extrusion_height=None, solid=False):
    v_data = MODEL_DATA.vertices[vidx]

    base_fix = square(FIXTURE_SIZE, center=True)

    for edge in v_data.edges:
        print("")
        point = Point3(*[inch(p) for p in edge.vector_ingress])
        if debug:
            to_origin: LineSegment3 = point.connect(Point3(0, 0, 0))
            yield draw_segment(to_origin), None

        extrusion_height = extrusion_height or inch(1.5)

        print("Fixture mag:", point.magnitude())
        print("Fixture mag - CORE:", point.magnitude() - CORE_SIZE)
        to_origin_line: LineSegment3 = point.connect(Point3(*ORIGIN))
        norm_direction = (point - ORIGIN).normalized()
        print("Normalized dir:", norm_direction)
        to_core_dist = to_origin_line.length

        # Transform to origin, but look towards the normalized direction but reflect (so its recv the edge).
        reflected_dir = norm_direction.reflect(norm_direction)
        midpoint = (
            Point3(extrusion_height / 3, extrusion_height / 3, extrusion_height / 3)
            * norm_direction
        )
        label_point = Point3(extrusion_height, extrusion_height, extrusion_height) * norm_direction
        pin_point = (
            Point3(extrusion_height / 2, extrusion_height / 2, extrusion_height / 2)
            * norm_direction
        )

        fix = base_fix.copy()
        inspect_fix = base_fix.copy()
        if not solid:
            fix = dotSCAD.hollow_out.hollow_out(shell_thickness=3)(fix)

        fix = linear_extrude(extrusion_height)(fix)
        inspect_fix = linear_extrude(extrusion_height)(inspect_fix)

        print(extrusion_height / 3)

        # Calc distance from origin (aka, joint vertex) to determine how much less of an edge we need.
        dist = Point(*ORIGIN).distance(Point(midpoint.x, midpoint.y, midpoint.z))
        print("Distance from start of fixture to origin:", dist)
        edge.length = edge.length - dist

        print(
            f"Rendering Edge {edge}:{edge.length_in}'' -> {MODEL_DATA.get_edge_target_vertex(edge).label} @ {point} (H: {extrusion_height}, D: {to_core_dist})"
        )

        fix = transform_to_point(fix, dest_point=midpoint, dest_normal=reflected_dir)
        inspect_fix = transform_to_point(
            inspect_fix, dest_point=midpoint, dest_normal=reflected_dir
        )

        inspect_data = None
        verts_by_face = None
        face_verts = None
        with utils.TemporaryScadWorkspace(
            scad_objs=[("fix", union()(inspect_fix), "stl")]
        ) as tmpdata:
            tmp_path, tmp_files = tmpdata
            utils.exec_pymesh(
                "collect_verts", tmp_files[0][-1].name, "out.json", host_mount=tmp_path
            )
            inspect_data = json.loads((tmp_path / "out.json").read_text())
            verts_by_face = inspect_data["verts_by_face"]
            face_verts = inspect_data["verts"]

        first_verts = [Point(i) for i in face_verts]

        first_face_plane = Plane(*first_verts)
        last_face_plane = None
        last_face_verts = None
        last_dist = 0
        for fidx, verts in verts_by_face:
            test_verts = [Point(v) for v in verts]
            test_plane = Plane(*test_verts)
            dist = first_face_plane.distance(test_plane)
            print(fidx, verts)
            print(f"first to {fidx}", dist)
            if abs(Float(dist)) >= abs(Float(last_dist)):
                last_dist = dist
                last_face_plane = test_plane
                last_face_verts = test_verts

        cp1 = Point(last_face_verts[0])
        fcp1 = first_verts[0]
        coplaner_points: List[Point] = [
            Point(i) for i in last_face_verts[1:] if Point.are_coplanar(cp1, Point(i), fcp1)
        ]
        print("Coplaner:", coplaner_points)
        cp2 = max(coplaner_points, key=lambda p: cp1.canberra_distance(p))

        face_midpoint = cp1.midpoint(cp2)

        if not solid:
            # pin hole for small nail or M3
            pz = translate([face_midpoint.x, face_midpoint.y, face_midpoint.z])(sphere(r=5))
            pz.modifier = "%"
            fix += pz
            for point in last_face_verts:
                p = translate(point)(sphere(r=5))
                p.modifier = "%"
                fix += p

        print("loaded inspect data:", inspect_data)

        if not solid:
            label = label_size(
                f"{MODEL_DATA.get_edge_target_vertex(edge).label}\n{round(edge.length_in, 2)}",
                halign="center",
                valign="center",
                depth=1.5,
                size=6,
                width=9,
                center=False,
            )[0]
            np_reflected_dir = np.array((reflected_dir.x, reflected_dir.y, reflected_dir.z))
            np_up_vec = np.array((0, 0, 1))
            perp_normal = vg.perpendicular(np_reflected_dir, np_up_vec)
            print("Perp Normal: ", perp_normal)

            targ_normal = BACK_VEC
            slide_dir = forward

            abs_y = abs(midpoint.y)
            abs_x = abs(midpoint.x)
            abs_z = abs(midpoint.z)
            if abs_y >= abs_x and abs_y >= abs_z:
                targ_normal = LEFT_VEC
                slide_dir = right

            label = transform_to_point(
                label, dest_point=label_point, dest_normal=targ_normal, src_normal=reflected_dir
            )
            label = slide_dir(extrusion_height / 4 + 1.2)(label)

            fix -= label

        if debug:
            fix.modifier = "#"
        yield fix, midpoint, inspect_data


def assembly(vertex: int, *args, **kwargs):
    a = union()

    progress = kwargs.pop("progress", None)
    fixture_points: List[Point3] = []
    fixtures: List[OpenSCADObject] = []
    for fix, point in assemble_vertex(vertex, *args, **kwargs):
        fixtures.append(fix)
        if point:
            fixture_points.append(point)

    core = assemble_core(vertex, fixture_points, *args, **kwargs, progress=progress)
    for fix in fixtures:
        core += fix

    a += core
    if kwargs.get("debug", False):
        a += grid_plane(plane="xyz", grid_unit=inch(1))
    return a


def create_model(vidx: int, *args, **kwargs):
    a = assembly(vidx, *args, **kwargs)
    scad_render_to_file(a, file_header=f"$fn = {SEGMENTS};", include_orig_code=True)


def load_model(model_path: Path) -> utils.ModelInfo:
    global MODEL_DATA, MODEL_DATA_PATH
    MODEL_DATA_PATH = model_path
    data: utils.ModelInfo = pickle.loads(MODEL_DATA_PATH.read_bytes())
    MODEL_DATA = data["data"]
    return data["info"]


def generate(
    model_path: PathLike, vertices=tuple(), debug=False, render=False, keep=False, file_type="stl"
):
    """Generate joint model from given vertex."""
    info = load_model(model_path)
    if not any(vertices):
        vertices = tuple(range(info.num_vertices))
        print(f"[bold orange]Rendering: {info.num_edges} edges | {info.num_vertices} vertices")
        print(vertices)
    output_dir = ROOT.parent / "renders"
    output_dir.mkdir(exist_ok=True)
    with progress.Progress(
        utils.ParentSpinnerColumn(),
        progress.TextColumn("[bold white]{task.description}"),
        utils.ParentProgressColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        utils.ComputeTestResultsColumn(),
        progress.BarColumn(bar_width=None),
        utils.ComputeTestResultsTextColumn(),
        transient=True,
    ) as prog:
        task = prog.add_task("[green]Generating Models...", total=info.num_vertices)
        for vertex in vertices:
            if not render:
                return create_model(vertex, debug=debug)
            a = assembly(vertex, debug=debug, progress=prog)
            _, file_name = tempfile.mkstemp(suffix=".scad")
            file_path = Path(tempfile.gettempdir()) / file_name
            out_render = scad_render(a, file_header=f"$fn = {SEGMENTS};")
            file_path.write_text(out_render)
            render_name = f"joint-v{vertex}.{file_type}"
            render_path = output_dir / render_name
            proc = utils.openscad_cmd("-o", str(render_path), str(file_path))
            for line in iter(proc.stderr.readline, b""):
                outline = line.decode().rstrip("\n")
                prog.console.print(f"[grey42]{outline}")
            if keep:
                scad_path = render_path.with_suffix(".scad")
                shutil.move(file_path, scad_path)
            prog.update(task, advance=1)
