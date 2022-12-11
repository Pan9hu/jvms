#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

class Modify_Configuration:

    @staticmethod
    def modify(k:str,v:str):
        f = open(".jvms-config.ini", 'r', encoding="UTF-8")
        allines = f.readlines()
        f.close()
        content = tuple(allines)
        for value in content:
            row = value.strip()
            cols = row.split(" = ")
            if cols[0] == k:
                f = open(".jvms-config.ini", 'w+', encoding="UTF-8")
                for line in allines:
                    new = re.sub(cols[1], v, line)
                    f.writelines(new)
                    f.flush()
                f.close()

if __name__ == '__main__':
    pass
