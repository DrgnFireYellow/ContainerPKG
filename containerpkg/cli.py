import typer
from typing import Literal
import containermanager
import packagemanager
from rich import print

SUPPORTED_DISTROS = ["ubuntu", "fedora", "alpine"]

cli = typer.Typer()

@cli.command()
def initialize(distro: str):
    if distro in SUPPORTED_DISTROS:
        containermanager.download(distro)
    else:
        print(f"[bold red]ERROR: Unsuported distribution \"{distro}\"")

@cli.command()
def update_index(distro: str):
    if distro in SUPPORTED_DISTROS:
        packagemanager.update_index(distro)
    else:
        print(f"[bold red]ERROR: Unsuported distribution \"{distro}\"")

@cli.command()
def install(distro: str, package: str):
    if distro in SUPPORTED_DISTROS:
        packagemanager.install(distro, package)
    else:
        print(f"[bold red]ERROR: Unsuported distribution \"{distro}\"")

@cli.command()
def remove(distro: str, package: str):
    if distro in SUPPORTED_DISTROS:
        packagemanager.remove(distro, package)
    else:
        print(f"[bold red]ERROR: Unsuported distribution \"{distro}\"")

@cli.command()
def upgrade(distro: str, package: str):
    if distro in SUPPORTED_DISTROS:
        packagemanager.upgrade(distro, package)
    else:
        print(f"[bold red]ERROR: Unsuported distribution \"{distro}\"")

cli()