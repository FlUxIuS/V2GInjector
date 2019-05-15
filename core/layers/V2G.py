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

