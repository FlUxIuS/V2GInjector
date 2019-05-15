#!/usr/bin/env python
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
