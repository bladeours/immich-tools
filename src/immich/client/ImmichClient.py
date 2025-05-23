from datetime import datetime
from typing import NoReturn, TypeVar
import requests as r
from requests.exceptions import HTTPError
import logging
import sys
from dacite import Config, from_dict

from src.immich.model.Album import Album
from src.immich.model.Asset import Asset
from src.immich.model.AssignTagResponse import AssignTagResponse
from src.immich.model.Tag import Tag

T = TypeVar("T")


class ImmichClient:
    def __init__(self, url, api_key):
        self.log = logging.getLogger("immich-tools")
        self.url = url
        self.api_key = api_key

    def get_asset(self, id: str) -> Asset:
        """Returns asset of id \n
        path: /api/asssets/:id

        Parameters:
          id: id of the asset

        Returns:
          asset
        """
        r = self.__send_get(f"/api/assets/{id}")
        return self.__from_dict(data_class=Asset, data=r.json())

    def get_album(self, id: str) -> Album:
        """Returns album of id \n
        path: /api/albums/:id

        Parameters:
          id: id of the album

        Returns:
          album
        """
        r = self.__send_get(f"/api/albums/{id}")
        return self.__from_dict(Album, r.json())

    def get_all_tags(self) -> list[Tag]:
        """Returns all tags \n
        path: /api/tags

        Returns:
          list of tags
        """
        r = self.__send_get(f"/api/tags")
        tags_json = r.json()
        return [self.__from_dict(Tag, tag_json) for tag_json in tags_json]

    def assign_tag_to_assets(self, tagId: str, assetIds: list[str]) -> list[AssignTagResponse]:
        """assign tags to assets \n
        PUT /api/tags/{tagId}/assets

        Returns:
          Immich Response
        """
        r = self.__send_put(f"/api/tags/{tagId}/assets", data={"ids": assetIds})
        responses = r.json()
        return [self.__from_dict(AssignTagResponse, response)
                for response in responses]

    def create_tag(self, name: str, color = "", parentId = ""):
        data = {"name": name}
        if color and color != "":
          data["color"] = color
        if parentId and parentId != "":
          data["parentId"] = parentId
        r = self.__send_post(f"/api/tags", data = data)
    
    def __send_put(self, path: str, data: dict = {}):
        try:
            response = r.put(self.url + path, json=data, headers={"x-api-key": self.api_key})
            response.raise_for_status()
        except r.exceptions.HTTPError as err:
            self.__log_and_exit(err, path)
        return response

    def __send_get(self, path: str) -> r.Response:
        try:
            response = r.get(self.url + path, headers={"x-api-key": self.api_key})
            response.raise_for_status()
        except HTTPError as err:
            self.__log_and_exit(err, path)
        return response
      
    def __send_post(self, path: str, data: dict={}):
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

    def __from_dict(self, data_class: type[T], data: dict) -> T:
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
