#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from libcore.config.config import Config
import configparser

def jvmt():
    conf = Config()
    print(conf.set(key="lang",value="Chinese"))
    print(conf.get(key="lang"))
    print(conf.get_with_default(key="mirror",value="sb"))
    # conf = configparser.ConfigParser()
    # conf.read(".jvms-config.ini",encoding="UTF-8")
    # result = conf.items("app")
    # print(result[0])

if __name__ == '__main__':
    jvmt()