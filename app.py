#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from libcore.config.config import Config


def jvmt():
    conf = Config()
    print(conf.get(key="lang"))


if __name__ == '__main__':
    jvmt()