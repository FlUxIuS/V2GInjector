#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from core.layers.V2G import *
from libs.EXIdecoder import *
from core.Logs import *

class BasicWrapper(object):
    def __init__(self):
        pass

    @log_wrapper("CLIENT_OUTPUT", decodeEXI)
    def wrap_client(self, pkt):
        return (pkt, pkt.Payload)

    @log_wrapper("SERVER_OUTPUT", decodeEXI)
    def wrap_server(self, pkt):
        return (pkt, pkt.Payload)
