# -*- coding: utf-8 -*-

from scapy.all import *

class SECC_RequestMessage(Packet):
    name = "SECC_RequestMessage"
    fields_desc = [ ByteField("SecurityProtocol", 0x0),
                    ByteField("TransportProtocol", 0x0),
            ]

class SECC_ResponseMessage(Packet):
    name = "SECC_ResponseMessage"
    fields_desc = [ IP6Field("TargetAddress", "::"),
                    ShortField("TargetPort", 0),
                    ByteField("SecurityProtocol", 0x0),
                    ByteField("TransportProtocol", 0x0),
            ]

SECC_types = {  0x9000 : "SECC_RequestMessage",
                0x9001 : "SECC_ResponseMessage",
        }

class SECC(Packet):
    name = "SECC"
    fields_desc = [ ByteField("Version", 0x01),
                    ByteField("Inversion", 0xfe),
                    ShortEnumField("SECCType", 0, SECC_types),
                    IntField("PayloadLen", 0),
                ]

bind_layers( UDP, SECC, { "dport" : 15118 } )
bind_layers( UDP, SECC, { "sport" : 15118 } )
bind_layers( SECC, SECC_RequestMessage, { "SECCType" : 0x9000 } )
bind_layers( SECC, SECC_ResponseMessage, { "SECCType" : 0x9001 } )
