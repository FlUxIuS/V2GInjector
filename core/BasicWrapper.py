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
