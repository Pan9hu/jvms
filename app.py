#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from libcore.config.config import Config


def jvmt():
    conf = Config()
    # print(conf.get(key="publisher"))
    conf.set(key="lang",value="English")

if __name__ == '__main__':
    jvmt()