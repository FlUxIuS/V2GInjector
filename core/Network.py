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

import sys
import os

from core.Config import *
from core.Logs import log_hpgp
from layerscapy.HomePlugGP import *
from core.layers.SECC import *
from core.layers.V2G import *
from core.BasicWrapper import *
from core.PInterceptor import *

SERVER_TO_CLIENT = 0
CLIENT_TO_SERVER = 1

class Network(object):
    """
        Network Class to sniff and process packet, including PCAP captures
    """
    pcapfile = None
    interceptor = None
    hpgp = {}

    def __init__(self, interceptor=PInterceptor()):
        self.interceptor = interceptor

    def __SECCpeers(self, pkt, direction):
        """
            Save SECC peers information
            In(1): Scapy packet
            In(2): Int SERVER_TO_CLIENT or CLIENT_TO_SERVER direction
        """
        dest = pkt[IPv6].dst
        src = pkt[IPv6].src
        sport = {"UDP" : pkt.sport}
        dport = {"UDP" : pkt.dport}
        stype = "client"
        dtype = "server"
        if direction == SERVER_TO_CLIENT:
            stype = "server"
            dtype = "client"
        if src not in self.interceptor.peers:
            self.interceptor.peers[src] = {}
        if direction == SERVER_TO_CLIENT:
            if dest not in self.interceptor.peers:
                self.interceptor.peers[dest] = {}
            self.interceptor.peers[dest]["SECC"] = {"type" : dtype, "port" : dport}
        self.interceptor.peers[src]["SECC"] = {"type" : stype, "port" : sport}

    def __processSECC(self, pkt):
        """
            Process SECC packets
            In(1): Scapy packet
        """
        if pkt.haslayer("SECC_RequestMessage"):
            self.__SECCpeers(pkt, CLIENT_TO_SERVER)
        if pkt.haslayer("SECC_ResponseMessage"):
            self.__SECCpeers(pkt, SERVER_TO_CLIENT)
            address = pkt.TargetAddress
            if address not in self.interceptor.peers:
                self.interceptor.peers[address] = {}
            self.interceptor.peers[address]["V2G"] = {"type" : "server", "port" : pkt.TargetPort}

    def processV2G(self, pkt, ports=None):
        """
            Process V2G packet
            In(1): Scapy packet
            In(2): list of known ports to process #TODO
        """
        payload = None
        if pkt[IPv6].src in self.interceptor.peers:
            if "V2G" in self.interceptor.peers[pkt[IPv6].src]:
                if pkt[TCP].sport == self.interceptor.peers[pkt[IPv6].src]["V2G"]["port"]:
                    if "V2G" not in self.interceptor.peers[pkt[IPv6].dst]:
                        self.interceptor.peers[pkt[IPv6].dst]["V2G"] = {"type":"server", "port":pkt[TCP].dport}
                    payload = V2GTP(pkt.load)
        if pkt[IPv6].dst in self.interceptor.peers:
            if "V2G" in self.interceptor.peers[pkt[IPv6].dst]:
                if pkt[TCP].dport == self.interceptor.peers[pkt[IPv6].dst]["V2G"]["port"]:
                    if "V2G" not in self.interceptor.peers[pkt[IPv6].src]:
                        self.interceptor.peers[pkt[IPv6].src]["V2G"] = {"type":"client", "port":pkt[TCP].sport}
                    payload = V2GTP(pkt.load)
        return payload

    @log_hpgp("NEW_HPGP_NETWORK")
    def __newHPGP(self, pkt, network):
        """
            Log new HomePlug GP networks
            In(1): Scapy packet
            In(2): Dict new network information
            Out: Tuple with Scapy packet and new network information
        """
        return (pkt, network)

    def processHPGP(self, pkt):
        """
            Process HomePlug GP packet
            In(1): Scapy packet
            Out: Scapy packet
        """
        if "CM_SLAC_MATCH_CNF" in pkt:
            varfield = pkt['CM_SLAC_MATCH_CNF'].VariableField
            nmk = varfield.NMK
            netid = varfield.NetworkID
            runid = varfield.RunID
            evseid = varfield.EVSEID
            evid = varfield.EVID
            newentry = {    "NMK" : nmk,
                            "RunID" : runid,
                            "EVSEID" : evseid,
                            "EVID" : evid,
                       }
            logentry = newentry
            logentry["NetID"] = netid
            if netid not in self.hpgp:
                self.hpgp[netid] = newentry
                return self.__newHPGP(pkt, logentry)
        return pkt 

    def analyse(self, pkt):
        """
            Packet analyser
            In(1): Scapy packet
            Out: Intercepted Scapy packet
        """
        new_pkt = pkt
        if pkt.haslayer("SECC"):
            self.__processSECC(pkt)
        elif pkt.haslayer("IPv6") and pkt.haslayer("TCP"):
            if int(pkt.flags) == 24:
                payload = self.processV2G(pkt)
                del(new_pkt[Raw])
                new_pkt /= payload
        elif pkt.haslayer("HomePlugAV"):
            self.processHPGP(pkt)
        return self.interceptor.intercept(new_pkt)

    def pcap(self, pcapfile):
        """
            PCAP processor
            In(1): String PCAP file path
        """
        r = rdpcap(pcapfile)
        for p in r:
            self.analyse(p)

    def sniff(self, iface):
        """
            Sniffer
            In(1): String device interface to sniff
        """
        sniff(prn=self.analyse, iface=iface, L2socket=conf.L2socket)
