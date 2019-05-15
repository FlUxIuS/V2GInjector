# -*- coding: utf-8 -*-

#    V2GInjector is a tool to penetrate V2G network through PowerLine, monitor and inject traffic
#    Copyright (C) 2019  Sebastien Dudek (@FlUxIuS)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from core.Singleton import Singleton
import configparser

class Config(Singleton):
    config = {}
    extra = None
    verboselogs = False

    def parse_config(cls, config_path="config/default.cfg"):
        """
            Configuration parser
            In(1): String configuration path
        """
        config = configparser.ConfigParser()
        config.read(unicode(config_path))
        for s in config:
            cls.config[s] = {}
            for k in config[s]:
                cls.config[s][k] = config[s][k] 
