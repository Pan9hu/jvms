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
    __config = None

    def __init__(self,config:Config = None):
        try:
            self.__config = Config()
            mirror = self.__config.get(key="mirror")
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

        if StringUtil.is_empty(index_version):
            return None

        return index_version

    def get_publisher(self)->str | None:
        publisher = self.__config.get("publisher").lower().strip()
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

        return index_publisher

    def get_update_time(self)->str | None:
        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_reponse = response.json()
        update_time = json_reponse['update-time']

        if StringUtil.is_empty(update_time):
            return None

        return update_time

    def get_app_version_by_publisher(self,publisher:str)->tuple:
        pass

    def get_app(self,publisher:str,version:str)->tuple:
        pass

if __name__ == '__main__':
    pass
