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

from __future__ import print_function

from core.Config import *
from layerscapy.HomePlugGP import *
from core.layers.SECC import *
from core.layers.V2G import *

from libs.EXIdecoder import *
from colorama import Fore, Back, Style 

config = Config()
config.verboselogs = True

class log_wrapper(object):
    def __init__(self, detail, decoder_fct=None):
        self.detail = detail
        self.decoder_fct = decoder_fct

    def print_dec(self, payload):
        if self.decoder_fct is not None:
            print (Fore.GREEN + "[Decoded packet]")
            print (self.decoder_fct(payload))
            print (Style.RESET_ALL)

    def __call__(self, f):
        def wrapped(*args, **kargs):
            config = Config()
            toreturn = f(*args, **kargs)
            if config.verboselogs is True:
                if len(toreturn) > 0:
                    print (repr(toreturn[0]))
                    self.print_dec(toreturn[1])
            return toreturn
        return wrapped

class log_hpgp(log_wrapper):
    def print_dec(self, payload):
        print (Fore.YELLOW + "[New HPGP network spotted!]")
        for k,v in payload.items():
            print ("- %s: %s" % (k, repr(v)))
        print (Style.RESET_ALL)
