# -*- coding: utf-8 -*-

from core.Singleton import Singleton

class Config(Singleton):
    config = {}
    extra = None
    verboselogs = False

    def parse_config(cls):
        pass
