#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import binascii

decoder_service = "http://localhost:9000"

def decodeEXI(data):
    data = binascii.hexlify(data)
    r = requests.post(  decoder_service,
                        headers={"Format":"EXI"},
                        data=data)
    return r.text

def encodeEXI(data):
    r = requests.post(  decoder_service,
                        headers={"Format":"XML"},
                        data=data)
    return r.text

