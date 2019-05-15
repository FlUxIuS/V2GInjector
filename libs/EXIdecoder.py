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

import requests
from core.InjExceptions import *
from core.Config import *

def sendpost(data, dformat):
    host = Config.config["V2GService"]["host"]
    port = Config.config["V2GService"]["port"]
    decoder_service = "http://%s:%s" % (host, port)
    try:
        r = requests.post(  decoder_service,
                            headers={"Format":dformat},
                            data=data)
        return r.text
    except requests.ConnectionError:
        raise DecodeError("Could'nt decode "+dformat+" data", "The V2G web server is not responding.")

def decodeEXI(data):
    import binascii
    return sendpost(binascii.hexlify(data), "EXI")

def encodeEXI(data):
    return sendpost(data, "XML")
