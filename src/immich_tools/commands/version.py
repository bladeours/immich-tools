import click
import immich_tools


@click.command()
def version():
    """shows version"""
    click.echo(immich_tools.__version__)
