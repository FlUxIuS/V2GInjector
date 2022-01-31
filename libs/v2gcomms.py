from core.layers.V2G import *
from socket import *

def v2gsendexi(payload, host, port):
    import binascii
    payload = binascii.unhexlify(payload)
    addrinfo = getaddrinfo(host, port, AF_INET6, SOCK_STREAM)
    (family, socktype, proto, canonname, sockaddr) = addrinfo[0]
    s = socket(family, socktype, proto)
    s.connect(sockaddr)
    v2gpkt = V2GTP(Version=1,Invers=254,PayloadType=32769, PayloadLen=len(payload),
                     Payload=payload)
    s.send(bytes(v2gpkt))
    s.close()
