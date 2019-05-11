# -*- coding: utf-8 -*-

from scapy.all import *

V2GTP_PayloadTypes = { 0x8001 : "EXI",
        }

class V2GTP(Packet):
    name = "V2GTP"
    fields_desc = [ ByteField("Version", 0x01),
                    ByteField("Invers", 0xfe),
                    ShortEnumField("PayloadType", 0x8001, V2GTP_PayloadTypes),
                    FieldLenField("PayloadLen", 0, count_of="Payload", fmt="I"),
                    StrLenField("Payload", "", length_from = lambda pkt: pkt.PayloadLen),
            ]

