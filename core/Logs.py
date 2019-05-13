# -*- coding: utf-8 -*-

from core.Config import *
from layerscapy.HomePlugGP import *
from core.layers.SECC import *
from core.layers.V2G import *

config = Config()
config.verboselogs = True

class log_wrapper(object):
    def __init__(self, detail, decoder_fct=None):
        self.detail = detail
        self.decoder_fct = decoder_fct
    def __call__(self, f):
        def wrapped(*args, **kargs):
            config = Config()
            toreturn = f(*args, **kargs)
            if config.verboselogs is True:
                if len(toreturn) > 0:
                    if self.decoder_fct is not None:
                        results = self.decoder_fct(toreturn)
                    else:
                        print toreturn
            return toreturn
        return wrapped
