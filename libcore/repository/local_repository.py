#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from libcore.exception.not_support_repository_indexer_exception import NotSupportRepositoryIndexException


class LocalRepository:
    __indexer = None

    def __init__(self,indexer:Index):
        if indexer is None:
            raise NotSupportRepositoryIndexerException("Local Repository indexer is null")
        self.__indexer = indexer



if __name__ == '__main__':
    pass
