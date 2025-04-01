import click
from src.commands import merge_xmp, refresh_album_metadata, run_job
import logging
from datetime import datetime

log = logging.getLogger("immich-tools")
log.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)-5s - %(message)s")

file_handler = logging.FileHandler(datetime.now().strftime('logs/log_%d_%m_%Y.log'))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

log.addHandler(console_handler)


@click.group()
@click.option("-d", "--debug", is_flag=True, help="Enable debug mode")
@click.option("-l", "--log-file", is_flag=True, help="Saves logs to file")
@click.pass_context
def main(ctx, debug:bool, log_file: bool):
    """Tools for immich"""
    ctx.ensure_object(dict)
    if log_file:
        log.addHandler(file_handler)
    if debug:
        log.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        log.debug("Debug mode is ON")
    log.info("Running immich-tools")
        
main.add_command(refresh_album_metadata.refresh_album_metadata)
main.add_command(merge_xmp.merge_xmp)
main.add_command(run_job.run_job)