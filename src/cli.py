import click
from src.commands import add, refresh_album_metadata
import logging

log = logging.getLogger("immich-tools")
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)


@click.group()
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.pass_context
def main(ctx, debug):
    """Tools for immich"""
    ctx.ensure_object(dict)
    if debug:
        log.setLevel(logging.DEBUG)
        log.debug("Debug mode is ON")
    pass

main.add_command(refresh_album_metadata.refresh_album_metadata)
main.add_command(add.add)