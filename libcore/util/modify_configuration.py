#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser

class Modify_Configuration:

    @staticmethod
    def modify(k:str,v:str):
        config = configparser.ConfigParser()
        config.read('.jvms-config.ini',encoding="UTF-8")
        config.set('app', k, v)
        config.write(open('.jvms-config.ini',"w",encoding="UTF-8"))


if __name__ == '__main__':
    pass
