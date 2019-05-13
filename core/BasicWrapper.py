#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from core.layers.V2G import *
from libs.EXIdecoder import *
from core.Logs import *

class BasicWrapper(object):
    def __init__(self):
        pass

    @log_wrapper("CLIENT_OUTPUT")
    def wrap_client(self, pkt):
        return decodeEXI(pkt.Payload)

    @log_wrapper("SERVER_OUTPUT")
    def wrap_server(self, pkt):
        return decodeEXI(pkt.Payload)
