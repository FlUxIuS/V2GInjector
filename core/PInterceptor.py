#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from core.layers.V2G import *
from core.BasicWrapper import *

class PInterceptor(object):
    peers = None
    wrapper = None

    def __init__(self, wrapper=BasicWrapper()):
        self.wrapper = wrapper
        self.peers = {}

    def intercept(self, pkt):
        wrapper = None
        if pkt.haslayer("V2GTP"):
            wrapper = self.wrapper.wrap_client
            if pkt[IPv6].dst in self.peers:
                if self.peers[pkt[IPv6].dst]["V2G"]["type"] == "server":
                    wrapper = self.wrapper.wrap_server
            if pkt[IPv6].src in self.peers:
                if self.peers[pkt[IPv6].src]["V2G"]["type"] == "server":
                    wrapper = self.wrapper.wrap_server
        if wrapper is not None:
            wrapper(pkt)
