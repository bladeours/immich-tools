from datetime import datetime, timezone
from typing import NoReturn, TypeVar
import requests as r
from requests.exceptions import HTTPError
import logging
import sys
from dacite import Config, from_dict

T = TypeVar("T")


class Utils:
    def __init__(self, url, api_key):
        self.log = logging.getLogger("immich-tools")
        self.url = url
        self.api_key = api_key

    def send_delete(self, path: str, data: dict):
        try:
            response = r.delete(self.url + path, json=data, headers={"x-api-key": self.api_key})
            response.raise_for_status()
        except r.exceptions.HTTPError as err:
            self.__log_and_exit(err, path)
        return response

    def datetime_to_str(self, datetime: datetime) -> str:
        dt = datetime.now(timezone.utc)
        formatted = dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        return formatted

    def send_multipart(self, path: str, files, data):
        try:
            response = r.post(self.url + path, files=files, headers={"x-api-key": self.api_key}, data=data)
            response.raise_for_status()
        except r.exceptions.HTTPError as err:
            self.__log_and_exit(err, path)
        return response

    def send_put(self, path: str, data: dict = {}):
        try:
            response = r.put(self.url + path, json=data, headers={"x-api-key": self.api_key})
            response.raise_for_status()
        except r.exceptions.HTTPError as err:
            self.__log_and_exit(err, path)
        return response

    def send_get(self, path: str) -> r.Response:
        try:
            response = r.get(self.url + path, headers={"x-api-key": self.api_key})
            response.raise_for_status()
        except HTTPError as err:
            self.__log_and_exit(err, path)
        return response

    def send_post(self, path: str, data: dict = {}):
        try:
            response = r.post(self.url + path, json=data, headers={"x-api-key": self.api_key})
            response.raise_for_status()
        except r.exceptions.HTTPError as err:
            self.__log_and_exit(err, path)
        return response

    def __snake_to_camel(self, name: str) -> str:
        components = name.split("_")
        s = components[0] + "".join(x.title() for x in components[1:])
        return s

    def from_dict(self, data_class: type[T], data: dict) -> T:
        return from_dict(
            data_class=data_class,
            data=data,
            config=Config(
                type_hooks={datetime: lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))},
                convert_key=self.__snake_to_camel,
            ),
        )

    def __log_and_exit(self, err: HTTPError, path: str) -> NoReturn:
        self.log.error(f"got error for request {self.url + path}: {err}")
        sys.exit(-1)
