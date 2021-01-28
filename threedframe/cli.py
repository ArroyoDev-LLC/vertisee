# -*- coding: utf-8 -*-

"""Console script for 3DFrame."""
import sys
from pathlib import Path

import click
from rich import print

from threedframe import joint, utils


@click.group()
def main():
    """3dframe Cli Entrypoint."""


@main.command()
@click.option("-d", "--debug", is_flag=True, default=False, help="Enable debug mode.")
@click.option(
    "-r", "--render", is_flag=True, default=False, help="Render to .STL or provided file type."
)
@click.option("-k", "--keep", is_flag=True, default=False, help="Keep SCAD Files.")
@click.option(
    "-f",
    "--file-type",
    default="stl",
    help="Exported file type.",
)
@click.argument(
    "model_data",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
)
@click.argument("vertices", type=int, nargs=-1)
def generate(model_data, vertices=tuple(), *args, **kwargs):
    """Generate joint model from given vertex."""
    if not any(vertices):
        print("[bold orange]No vertices were provided.")
        click.confirm("Would you like to render ALL vertices?", abort=True)
    joint.generate(Path(model_data), vertices, *args, **kwargs)


@main.command()
@click.argument(
    "model_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
def compute(model_path: Path):
    """Compute vertices/edge data from blender model."""
    model_path = Path(model_path)
    script_path = Path(__file__).parent / "compute.py"
    assert script_path.exists(), "Failed to find script path."
    data_path = model_path.with_suffix(".pkl")
    utils.exec_blender_script(Path(model_path), script_path, data_path)
    print("[bold green]✔ Done!")
    print(f"[bold white]Data written to: [cyan]{data_path.absolute()}")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
