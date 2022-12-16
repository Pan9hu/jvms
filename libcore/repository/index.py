#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
import requests

from libcore.config.config import Config
from libcore.util.string_util import StringUtil
from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.exception.indexer_init_failed_exception import IndexerInitFailedException


class App:
    __publisher = None
    __version = None
    __os = None
    __arch = None
    __dist = None
    __checksum_alog = None
    __checksum_content = None
    __file = None

    # TODO Getter/Setter
    def get_file(self)->str:
        return self.__file

class Index:
    """
    用于访问 GitHub 存储库或者镜像源的 Index 文件（Json）。
    """
    __index_json = "index.json"
    __mirror_url = ""


    def __init__(self,config : Config = None):
        try:
            config = Config()
            mirror = config.get(key="mirror")
            if mirror[-1] != '/':
                self.__mirror_url = mirror + '/' + self.__index_json
            else:
                self.__mirror_url = mirror + self.__index_json
        except ConfigKeyNotExistException as e:
            raise IndexerInitFailedException("Can not read mirror from config file, because: {}".format(e))

    def get_version(self)->str | None:
        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_response = response.json()
        index_version = json_response['version']

        return None if StringUtil.is_empty(index_version) else index_version

    def get_publisher(self)->str | None:
        list_publishers = []
        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_response = response.json()
        index_publishers = response.json()['apps']
        for i in range(len(index_publishers)):
            app_publisher = response.json()['apps'][i]
            for index_publisher in app_publisher:
                list_publishers.append(index_publisher)

        return list_publishers if len(list_publishers) >0 else None

    def get_update_time(self)->str | None:
        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_reponse = response.json()
        update_time = json_reponse['update-time']

        return None if StringUtil.is_empty(update_time) else update_time

    def get_app_version_by_publisher(self,publisher:str)->tuple | None:
        if StringUtil.is_empty(publisher):
            return None
        publisher = publisher.strip().lower()

        list_version_for_publisher = []
        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_response = response.json()
        index_publishers = response.json()['apps']
        for i in range(len(index_publishers)):
            app_publisher = response.json()['apps'][i]
            if publisher in app_publisher:
                index_publisher = app_publisher[publisher]

        if StringUtil.is_empty(index_publisher):
            return None

        mirror = self.__mirror_url.split(self.__index_json)
        url = mirror[0] + index_publisher
        response = requests.get(url)
        if response.status_code != 200:
            return None

        versions_json = response.json()
        for version in versions_json:
            list_version_for_publisher.append(version)

        return tuple(list_version_for_publisher) if len(list_version_for_publisher) >0 else None

    def get_app(self,publisher:str,version:str)->tuple | None:
        if StringUtil.is_empty(publisher):
            return None
        if StringUtil.is_empty(version):
            return None
        publisher = publisher.strip().lower()
        version = version.strip()

        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_response = response.json()
        index_publishers = response.json()['apps']
        for i in range(len(index_publishers)):
            app_publisher = response.json()['apps'][i]
            if publisher in app_publisher:
                index_publisher = app_publisher[publisher]
        print(index_publisher)
        if StringUtil.is_empty(index_publisher):
            return None

        mirror = self.__mirror_url.split(self.__index_json)
        url = mirror[0] + index_publisher
        response = requests.get(url)
        if response.status_code != 200:
            return None

        list_app = []
        versions_json = response.json()
        index_version = versions_json[version]
        mirror = url.split(index_publisher)
        url = mirror[0] + index_version
        response = requests.get(url)
        if response.status_code != 200:
            return None

        apps_json = response.json()
        for i in range(len(apps_json)):
            app = apps_json[i]
            list_app.append(app)

        return tuple(list_app) if len(list_app) >0 else None


if __name__ == '__main__':
    pass
