#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import requests
import click
import os
import shutil
from libcore.config.config import Config
from libcore.repository.index import Index
import configparser



# @click.group()
def jvms():
    i = Index()
    print(i.get_publisher())
    # print(i.get_version())
    # print(i.get_update_time())
    print(i.get_app_version_by_publisher('orAcle     '))
    print(i.get_app('orAcle     ','17.0.5        '))


    # url = 'http://192.168.3.11/apps/oracle/versions/17.0.5.json'
    # b = requests.get(url).json()
    # print(b)
    # l = len(b)
    # print(l)
    # for i in range(l):
    #     app = b[i]
    #     print(app)

    # c = [{'oracle': 'apps/oracle/index.json'}, {'amazon': 'apps/amazon/index.json'}]
    # l = len(c)
    # for j in range(l):
    #     b = c[j]
    #     for i in b:
    #         print(i)
    # # pass
    # conf = Config()
    # mirror = conf.get(key="mirror")
    # Json = 'index.json'
    # mirror = "http://192.168.3.11"
    # print(mirror[-1])
    # if mirror[-1] != '/':
    #     mirror_url = mirror + '/' + Json
    # else:
    #     mirror_url = mirror + Json
    # print(mirror)
    # response = requests.get(mirror_url)
    # print(response.json())
    # print(type(response.json()))
    # print(response.json()['apps'])
    # print(type(response.json()['apps']))
    # l = len(response.json()['apps'])
    # print(l)
    # a = 'amazon'
    # for i in range(l):
    #     s = response.json()['apps'][i]
    #     if a in s:
    #         print(s[a])
        # print(type(s))
        # print(s)
    # print(conf.get_with_default(key="lang", defalut="a"))
    # print(conf.set(key="lang",value="zh_CN"))
    # print(conf.get(key="lang"))
    # print(conf.get(key="publisher"))
    # print(conf.set(key="publisher", value="Amazon"))
    # print(conf.get(key="publisher"))
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