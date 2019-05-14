# -*- coding: utf-8 -*-

import sys
import os
from core.Config import *

config = Config()
config.parse_config("config/default.cfg")
sys.path.append(os.path.abspath(Config.config["Injector"]["homeplugpwn_path"]))

__all__ = ["BasicWrapper", "PInterceptor", "Logs", "Config", "Network"]
