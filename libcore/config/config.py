#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from libcore.util.modify_configuration import Modify_Configuration
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
        "you"
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
        self.__jvms_config.__next__()
        content = tuple(self.__jvms_config.readlines())
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

        if key == self.__allow_config_keys[0]:
            if value not in self.__allow_config_publishers:
                raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))
            Modify_Configuration.modify(k=key,v=value)
        elif key == self.__allow_config_keys[1]:
            if value not in self.__allow_config_mirrors:
                raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))
            Modify_Configuration.modify(k=key, v=value)
        elif key == self.__allow_config_keys[2]:
            if value not in self.__allow_config_languages:
                raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))
            Modify_Configuration.modify(k=key, v=value)

        return True

    def get_with_default(self,key:str,value:str,default:str):
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
