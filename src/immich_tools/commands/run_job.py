import click
import logging

from immich_tools.immich.client.ImmichClient import ImmichClient

log = logging.getLogger("immich-tools")


@click.command()
@click.option("-k", "--api-key", required=True, envvar="IMMICH_API_KEY")
@click.option("-u", "--url", required=True, envvar="IMMICH_URL")
@click.argument("job_name")
def run_job(api_key, url, job_name):
    """Runs job, possible values: thumbnailGeneration, metadataExtraction,
    videoConversion, faceDetection, facialRecognition, smartSearch, duplicateDetection,
    backgroundTask, storageTemplateMigration, migration, search, sidecar, library, notifications, backupDatabase"""
    log.debug(f"immich url: {url}")
    immich = ImmichClient(url, api_key)
    immich.utils.send_put(path=f"/api/jobs/{job_name}", data={"command": "start", "force": True}).json()
    log.debug(f"running job: {job_name}")
    log.info("success")
