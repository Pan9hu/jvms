#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from libcore.config.config import Config
import configparser

def jvmt():
    # conf = Config()
    # print(conf.set(key="lang",value="Chinese"))
    # print(conf.get(key="mirror"))
    # print(conf.get_with_default(key="mirror",defalut="ok"))
    # conf = configparser.ConfigParser()
    # conf.read(".jvms-config.ini",encoding="UTF-8")
    # result = conf.items("app")
    # print(result[0])
    config = configparser.ConfigParser()
    config.read(".jvms-config.ini",encoding="UTF-8")

    for k,v in config.items("app"):
        print(v)

if __name__ == '__main__':
    jvmt()