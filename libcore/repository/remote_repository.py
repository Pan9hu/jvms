#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from libcore.repository.index import App
from libcore.repository.index import Index
from libcore.exception.not_support_system_type_exception import NotSupportSystemTypeException

class RemoteRepository:
    __indexer = None

    def __init__(self,indexer:Index):
        if indexer is None:
            raise NotSupportSystemTypeException("Remote Repository indexer is null")
        self.__indexer = indexer


    def get_file_by_app(self,app:App)->str:
        return app.get_file()

if __name__ == '__main__':
    pass
