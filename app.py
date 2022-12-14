#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import click
import os
import shutil
from libcore.config.config import Config
import configparser



@click.group()
def jvms():
    pass
    # conf = Config()
    # print(conf.get(key="lang"))
    # print(conf.set(key="lang",value="zh_CN"))
    # print(conf.get(key="lang"))
    # print(conf.get(key="mirror"))
    # print(conf.set(key="mirror", value="url"))
    # print(conf.get(key="mirror"))
    # print(conf.get_with_default(key="mirror",defalut="ok"))
    # # conf = configparser.ConfigParser()
    # conf.read(".jvms-config.ini",encoding="UTF-8")
    # result = conf.items("app")
    # print(result[0])
    # config = configparser.ConfigParser()
    # config.read(".jvms-config.ini",encoding="UTF-8")
    #
    # print(config.has_section("app"))
    # config.set("app",'mirror','')
    # config.write(open(".jvms-config.ini", 'r+', encoding="UTF-8"))
    # print(config.has_option("app","mirror"))

    # pwd = os.getcwd()
    # config_tpl = pwd+ "\\" +"assets\.jvms-config.ini.template"
    # print(config_tpl)
    #
    # A = "C:\\Users\\15893\\AppData\\Local\\jjvmm\\config\\.jvms-config.ini"
    # Dir = A.split(".jvms-config.ini")
    # print(Dir[0])
    # os.makedirs(r"{}".format(Dir[0]))
    # shutil.copy(config_tpl,A)


if __name__ == '__main__':
    jvms()