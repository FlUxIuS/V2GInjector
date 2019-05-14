# -*- coding: utf-8 -*-

from core.Singleton import Singleton
import configparser

class Config(Singleton):
    config = {}
    extra = None
    verboselogs = False

    def parse_config(cls, config_path="config/default.cfg"):
        config = configparser.ConfigParser()
        config.read(unicode(config_path))
        for s in config:
            cls.config[s] = {}
            for k in config[s]:
                cls.config[s][k] = config[s][k] 
