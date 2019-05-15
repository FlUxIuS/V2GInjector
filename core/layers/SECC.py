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
