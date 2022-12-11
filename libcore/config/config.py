#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser
from libcore.util.modify_configuration import Modify_Configuration
from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.exception.config_value_not_in_range_exception import ConfigValueNotInRangeException
from libcore.util.string_util import StringUtil


class Config:
    """
    配置
    """

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

    __default = [__allow_config_publishers, __allow_config_mirrors, __allow_config_languages]

    def get(self,key:str) -> str:
        """
        获取配置项
        :param key: Key
        :return: Value
        """
        self.__key_check(key=key)
        config = configparser.ConfigParser()
        config.read('.jvms-config.ini',encoding="UTF-8")
        return (config.get('app',key))

    def set(self,key:str,value:str)-> bool:
        """
        设置配置项
        :param key: Key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """
        self.__key_check(key=key)
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

    def get_with_default(self,key:str, value:str) ->str:
        """
        获取配置项，如果这个配置项的值为空，那么返回 default
        :param key: Key
        :param value: Value
        :return: Value
        """
        self.__key_check(key=key)
        self.__key_check(key=key)
        config = configparser.ConfigParser()
        config.read('.jvms-config.ini', encoding="UTF-8")
        cur_value = config.get('app', key)
        if cur_value == value:
            return value
        elif len(cur_value) == 0:
            if key == "publisher":
                return ("publisher's default: {}".format(self.__default[0]))
            if key == "mirror":
                return ("mirror's default: {}".format(self.__default[1]))
            if key == "lang":
                return ("lang's default: {}".format(self.__default[2]))
        else:
            return "当前配置项的值为：{}".format(cur_value)


    def __key_check(self,key:str) -> bool:
        """
        检查 Key 如果为空或不在配置项范围内，那么抛出异常
        :param key:
        :return: 如果不为空且在配置项范围内，那么返回 True
        """
        if StringUtil.is_empty(s=key):
            raise ConfigKeyNotExistException("{} is not in config file, the key is empty.".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{} is not in config file, the key is irrational.".format(key))

        return True


if __name__ == '__main__':
    pass
