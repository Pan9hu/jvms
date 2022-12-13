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

class Index:
    """
    用于访问 GitHub 存储库或者镜像源的 Index 文件（Json）。
    """
    __index_json = "index.json"
    __mirror_url = ""

    def __init__(self,config:Config = None):
        # TODO 根据环境变量和配置文件读取镜像源
        try:
            mirror = config.get("mirror")
            self.__mirror_url

    def get_version(self)->str:
        pass

    def get_publisher(self)->str:
        pass


    def get_update_time(self)->str:
        pass

    def get_app_version_by_publisher(self,publisher:str)->tuple:
        pass

    def get_app(self,publisher:str,version:str)->tuple:
        pass

if __name__ == '__main__':
    pass
