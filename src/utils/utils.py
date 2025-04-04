import requests as r
import logging
from os import sys

log = logging.getLogger("immich-tools")

def send_get(path: str, url: str, api_key: str):
  try:
    response =  r.get(url + path, headers={"x-api-key": api_key})
    response.raise_for_status()
  except r.exceptions.HTTPError as err:
    log.error(f"got error for request {url + path}: {err}")
    sys.exit(-1)
  return response


def send_post(path: str, url:str, api_key:str, data: dict={}):
  try:
    response = r.post(url + path, json=data, headers={"x-api-key": api_key})
    response.raise_for_status()
  except r.exceptions.HTTPError as err:
    log.error(f"got error for request {url + path}: {err}")
    sys.exit(-1)
  return response

def send_put(path: str, url:str, api_key:str, data: dict={}):
  try:
    response = r.put(url + path, json=data, headers={"x-api-key": api_key})
    response.raise_for_status()
  except r.exceptions.HTTPError as err:
    log.error(f"got error for request {url + path}: {err}")
    sys.exit(-1)
  return response