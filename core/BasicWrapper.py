#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from core.layers.V2G import *
from libs.EXIdecoder import *

class BasicWrapper(object):
    def __init__(self):
        pass

    def wrap_client(self, pkt):
        print decodeEXI(pkt.Payload)
        return pkt

    def wrap_server(self, pkt):
        print decodeEXI(pkt.Payload)
        return pkt
