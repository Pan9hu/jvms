#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.exception.config_value_not_in_range_exception import ConfigValueNotInRangeException
from libcore.util.string_util import StringUtil


class Config:
    """
    配置
    """
    __jvms_config = None

    __allow_config_keys = (
        "publisher",
        "mirror",
        "lang"
    )

    __allow_config_publishers = (
        "Oracle",
        "Amazon"
    )

    __allow_config_mirrors = (
        "sb",
        "you too"
    )

    __allow_config_languages = (
        "English",
        "Chinese"
    )


    def get(self,key:str) -> str:
        """
        获取配置项
        :param key: Key
        :return: Value
        """


        if StringUtil.is_empty(s=key):
            raise ConfigKeyNotExistException("{} is not in config file, the key is empty.".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{} is not in config file, the key is irrational.".format(key))

        self.__jvms_config = open(".jvms-config.ini",'r',encoding="UTF-8")
        self.__jvms_config.readline()
        content = tuple(self.__jvms_config.readlines())
        tmp = []
        for value in content:
            row = value.strip()
            cols = row.split(" = ")
            if cols[0] == key:
                self.__jvms_config.close()
                return cols[1]


    def set(self,key:str,value:str)-> bool:
        """
        设置配置项
        :param key: Key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """


        if StringUtil.is_empty(s=key):
            raise ConfigKeyNotExistException("{} is not in config file, the key is empty.".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{} is not in config file, the key is irrational.".format(key))

        if StringUtil.is_empty(s=value):
            raise ConfigValueNotInRangeException("{} is not in in range, the value is empty.".format(value))

        for allow_key in self.__allow_config_keys:
            print(allow_key)
            if  key == allow_key:
                if value not in self.__allow_config_languages:
                    raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))


        pass

    def get_with_default(self,key:str,value,default:str):
        """
        获取配置项，如果这个配置项的值为空，那么返回 default
        :param key: Key
        :param value: Value
        :param default: 默认值
        :return: value
        """

        pass




if __name__ == '__main__':
    pass
