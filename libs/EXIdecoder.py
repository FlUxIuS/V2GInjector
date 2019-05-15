#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    return sendpost(data, "EXI")

def encodeEXI(data):
    import binascii
    return sendpost(binascii.hexlify(data), "XML")
