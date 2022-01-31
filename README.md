![V2GInjector Logo](/images/logo.png)

Tool to penetrate V2G networks, monitor and inject packets to attack electric cars and charging stations.

## Publications

- Researches paper: https://www.sstic.org/media/SSTIC2019/SSTIC-actes/v2g_injector_playing_with_electric_cars_and_chargi/SSTIC2019-Article-v2g_injector_playing_with_electric_cars_and_charging_stations_via_powerline-dudek.pdf
- Slides from SSTIC 2019: https://www.sstic.org/media/SSTIC2019/SSTIC-actes/v2g_injector_playing_with_electric_cars_and_chargi/SSTIC2019-Slides-v2g_injector_playing_with_electric_cars_and_charging_stations_via_powerline-dudek.pdf
- Video recording from SSTIC 2019 (in French): https://static.sstic.org/videos2019/1080p/SSTIC_2019-06-07_P06.mp4

Support: contact the [Penthertz company](https://penthertz.com/) which is the owner of the project.

## Dependencies

### Software 

- Python 2, and Python 3
- Scapy
- Colorama for Python
- V2Gdecoder in submodules, that is already compiled and available here: https://github.com/FlUxIuS/V2Gdecoder/releases
- HomePlugPWN that is provided in submodules

To install Python dependencies, use `pip install -r requirements.txt` (or `pip3` as needed).

Submodules can be fetched as follows:
```
$ git submodule update --init --recursive
```

### Hardware

Any devices using the PowerLine-Communication Qualcomm Atheros 7k (QCA7k) series baseband (tested on QCA7420 and QCA7500). 
For wallplugs, next to the HomePlug logo, there is a text descripting plug's interoperability including HomePlug GP.

The tool has been tested with following devices:

* dLAN Green PHY eval board EU II (~150€)
* PLC Stamp Micro 2 Evaluation Board (Home Automation) (~300€)
* Devolo 1200+ (~50€) -> to rework if you want to bind it to CP lines -> dangerous to get access on TR+/- lines /!\
* Working on QCA7420 chips, but attenuation must be forced on EVSE side for the SLAC procedure
* TODO: test other devices with a QCA7k PLC baseband.

## Connections

The PowerLine Communication device could be plugged in three different ways:

* plugging it with an IEC 61851 or any compatible connector for your targeted car (that could be found in Alibaba)
* with an interception cable between the charging station and the car
* or using simply use a default PLC wallplug with a QCA7k connected to the same shared electrical network as the charging station(s) and the car(s). 

## How to use it

The tool can be started with the following interpreter as follows:
```
$ python V2GInjector

ooooo  oooo  ooooooo     ooooooo8  
 888    88 o88     888 o888    88  
  888  88        o888  888    oooo 
   88888      o888   o 888o    88  
    888    o8888oooo88  888ooo888  
ooooo             o88                         o8                        
 888  oo oooooo  oooo  ooooooooo8  ooooooo  o888oo ooooooo  oo oooooo   
 888   888   888  888 888oooooo8 888     888 888 888     888 888    888 
 888   888   888  888 888        888         888 888     888 888        
o888o o888o o888o 888   88oooo888  88ooo888   888o 88ooo88  o888o       
                 o88                                                    

~>>>
```

To collect data automatically, two methods are provided by Network class object:
* `Network().pcap(<pcap file>)`
* `Network().sniff(iface=<interface>)`

### Decoding V2G packet

First, the V2Gdecoder service must be running as follows:
```
$ java -jar V2Gdecoder.jar -w
```

Then, when calling `pcap()` or `sniff()` methods as follows, EXI data are simply decoded:
```
~>>> n=Network()
~>>> n.pcap("/tmp/emulated.pcapng")
<CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=0x86dd |<IPv6  version=6 tc=0 fl=36603 plen=76 nh=TCP hlim=64 src=fe80::3e2a:b4ff:3e5f:1a4 dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=54054 dport=62887 seq=1646944081 ack=4294522924 dataofs=8 reserved=0 flags=PA window=342 chksum=0xb60d urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1430435299, 1430435274))] |<V2GTP  Version=1 Invers=254 PayloadType=EXI PayloadLen=36 Payload='\x80\x00\xeb\xab\x93q\xd3K\x9by\xd1\x89\xa9\x89\x89\xc1\xd1\x91\xd1\x91\x81\x89\x99\xd2k\x9b:#+0\x02\x00\x00(\x00@' |>>>>
[Decoded packet]
<?xml version="1.0" encoding="UTF-8"?><ns4:supportedAppProtocolReq xmlns:ns4="urn:iso:15118:2:2010:AppProtocol" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema"><AppProtocol><ProtocolNamespace>urn:iso:15118:2:2013:MsgDef</ProtocolNamespace><VersionNumberMajor>2</VersionNumberMajor><VersionNumberMinor>0</VersionNumberMinor><SchemaID>10</SchemaID><Priority>1</Priority></AppProtocol></ns4:supportedAppProtocolReq>

<CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=0x86dd |<IPv6  version=6 tc=0 fl=218843 plen=44 nh=TCP hlim=64 src=fe80::3e2a:b4ff:3e5f:1a4 dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=62887 dport=54054 seq=4294522924 ack=1646944125 dataofs=8 reserved=0 flags=PA window=342 chksum=0xb5ed urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1430435378, 1430435299))] |<V2GTP  Version=1 Invers=254 PayloadType=EXI PayloadLen=4 Payload='\x80@\x02\x80' |>>>>
[Decoded packet]
<?xml version="1.0" encoding="UTF-8"?><ns4:supportedAppProtocolRes xmlns:ns4="urn:iso:15118:2:2010:AppProtocol" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema"><ResponseCode>OK_SuccessfulNegotiation</ResponseCode><SchemaID>10</SchemaID></ns4:supportedAppProtocolRes>

<CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=0x86dd |<IPv6  version=6 tc=0 fl=36603 plen=61 nh=TCP hlim=64 src=fe80::3e2a:b4ff:3e5f:1a4 dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=54054 dport=62887 seq=1646944125 ack=4294522936 dataofs=8 reserved=0 flags=PA window=342 chksum=0xb5fe urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1430435406, 1430435378))] |<V2GTP  Version=1 Invers=254 PayloadType=EXI PayloadLen=21 Payload="\x80\x98\x02\x00\x00\x00\x00\x00\x00\x00\x00\x11\xd0\x18pn\xd5\xac'X\x00" |>>>>
[Decoded packet]
<?xml version="1.0" encoding="UTF-8"?><ns7:V2G_Message xmlns:ns7="urn:iso:15118:2:2013:MsgDef" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema" xmlns:ns4="http://www.w3.org/2000/09/xmldsig#" xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"><ns7:Header><ns8:SessionID>0000000000000000</ns8:SessionID></ns7:Header><ns7:Body><ns5:SessionSetupReq><ns5:EVCCID>1C1BB56B09D6</ns5:EVCCID></ns5:SessionSetupReq></ns7:Body></ns7:V2G_Message>

<CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=0x86dd |<IPv6  version=6 tc=0 fl=218843 plen=69 nh=TCP hlim=64 src=fe80::3e2a:b4ff:3e5f:1a4 dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=62887 dport=54054 seq=4294522936 ack=1646944154 dataofs=8 reserved=0 flags=PA window=342 chksum=0xb606 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1430435411, 1430435406))] |<V2GTP  Version=1 Invers=254 PayloadType=EXI PayloadLen=29 Payload="\x80\x98\x02'\xe5\xc2N\x07\xc8h\xae\xd1\xe0 )\x15YM\x15%\x10\xb4\xc0\x1c\xfb\x1e\x1c\xc0\xa0" |>>>>
[Decoded packet]
<?xml version="1.0" encoding="UTF-8"?><ns7:V2G_Message xmlns:ns7="urn:iso:15118:2:2013:MsgDef" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema" xmlns:ns4="http://www.w3.org/2000/09/xmldsig#" xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"><ns7:Header><ns8:SessionID>9F9709381F21A2BB</ns8:SessionID></ns7:Header><ns7:Body><ns5:SessionSetupRes><ns5:ResponseCode>OK_NewSessionEstablished</ns5:ResponseCode><ns5:EVSEID>EVSEID-0</ns5:EVSEID><ns5:EVSETimeStamp>1557933159</ns5:EVSETimeStamp></ns5:SessionSetupRes></ns7:Body></ns7:V2G_Message>

<CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=0x86dd |<IPv6  version=6 tc=0 fl=36603 plen=53 nh=TCP hlim=64 src=fe80::3e2a:b4ff:3e5f:1a4 dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=54054 dport=62887 seq=1646944154 ack=4294522973 dataofs=8 reserved=0 flags=PA window=342 chksum=0xb5f6 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1430435414, 1430435411))] |<V2GTP  Version=1 Invers=254 PayloadType=EXI PayloadLen=13 Payload="\x80\x98\x02'\xe5\xc2N\x07\xc8h\xae\xd1\xb8" |>>>>
[Decoded packet]
<?xml version="1.0" encoding="UTF-8"?><ns7:V2G_Message xmlns:ns7="urn:iso:15118:2:2013:MsgDef" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema" xmlns:ns4="http://www.w3.org/2000/09/xmldsig#" xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"><ns7:Header><ns8:SessionID>9F9709381F21A2BB</ns8:SessionID></ns7:Header><ns7:Body><ns5:ServiceDiscoveryReq/></ns7:Body></ns7:V2G_Message>

<CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=0x86dd |<IPv6  version=6 tc=0 fl=218843 plen=83 nh=TCP hlim=64 src=fe80::3e2a:b4ff:3e5f:1a4 dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=62887 dport=54054 seq=4294522973 ack=1646944175 dataofs=8 reserved=0 flags=PA window=342 chksum=0xb614 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1430435419, 1430435414))] |<V2GTP  Version=1 Invers=254 PayloadType=EXI PayloadLen=43 Payload="\x80\x98\x02'\xe5\xc2N\x07\xc8h\xae\xd1\xc0\x01 \x04\x05QU\x88\x18\xda\x18\\\x99\xda[\x99\xc8\n\x10P\xcb\xd1\x10\xca@@ \x01\x03\x08H" |>>>>
[Decoded packet]
<?xml version="1.0" encoding="UTF-8"?><ns7:V2G_Message xmlns:ns7="urn:iso:15118:2:2013:MsgDef" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema" xmlns:ns4="http://www.w3.org/2000/09/xmldsig#" xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"><ns7:Header><ns8:SessionID>9F9709381F21A2BB</ns8:SessionID></ns7:Header><ns7:Body><ns5:ServiceDiscoveryRes><ns5:ResponseCode>OK</ns5:ResponseCode><ns5:PaymentOptionList><ns6:PaymentOption>ExternalPayment</ns6:PaymentOption></ns5:PaymentOptionList><ns5:ChargeService><ns6:ServiceID>1</ns6:ServiceID><ns6:ServiceName>EV charging (AC/DC)</ns6:ServiceName><ns6:ServiceCategory>EVCharging</ns6:ServiceCategory><ns6:FreeService>false</ns6:FreeService><ns6:SupportedEnergyTransferMode><ns6:EnergyTransferMode>AC_three_phase_core</ns6:EnergyTransferMode><ns6:EnergyTransferMode>AC_single_phase_core</ns6:EnergyTransferMode><ns6:EnergyTransferMode>DC_core</ns6:EnergyTransferMode><ns6:EnergyTransferMode>DC_extended</ns6:EnergyTransferMode><ns6:EnergyTransferMode>DC_combo_core</ns6:EnergyTransferMode></ns6:SupportedEnergyTransferMode></ns5:ChargeService></ns5:ServiceDiscoveryRes></ns7:Body></ns7:V2G_Message>
[...]
```

### Collected HPGP keys

Collected HomePlug GP keys are directly show when calling `pcap()` or `sniff()`:
```
~>>> n=Network()
~>>> n.sniff(iface="eth0")
[...]
[New HPGP network spotted!]
- EVSEID: '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
- NetID: '\xae\x20\x00\xff\x82\x02\x00'
- NMK: '\x43F\xc8\xaeT\xbf\xefs\x01\x84\x94\xf8\xc3\x17'
- EVID: '\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff'
- RunID: '\xef\x34C\xf5E\xe0\xa6\x01'
```
These data are stored in the `Network().hpgp` attribute.

This can then be used to configure your PLC device's PIB by dumping it with `plctool` and using `slac\pev` tool and profile file.

### Generate V2G packets

As it uses Scapy and extension layers, a V2G packet can be built using the same logic as Scapy:
```
~>>> ether = Ether()
~>>> ip = IPv6(dst="fe80::3e2a:b4ff:3e5f:1a4")
~>>> tcp = TCP(sport=6666, dport=54054, flags=24)
~>>> v2g=V2GTP()
~>>> packet = ether/ip/tcp/v2g
~>>> packet
<Ether  type=0x86dd |<IPv6  nh=TCP dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=6666 dport=54054 flags=PA |<V2GTP  |>>>>
```
But we need to push an EXI encoded payload in the V2GTP layer:
```
~>>> packet[V2GTP].show()
###[ V2GTP ]### 
  Version   = 1
  Invers    = 254
  PayloadType= EXI
  PayloadLen= 0
  Payload   = ''
```
To do that, as for the `analyse()` method call by `sniff()` and `pcap()` which uses `decodeEXI()` function to decode EXI data, a encoder function `encodeEXI` also exists to compress the XML payload to EXI:
```
~>>> xml = '<?xml version="1.0" encoding="UTF-8"?><ns7:V2G_Message xmlns:ns7="urn:iso:15118:2:2013:MsgDef" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema" xmlns:ns4="http://www.w3.org/2000/09/xmldsig#" xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"><ns7:Header><ns8:SessionID>0000000000000000</ns8:SessionID></ns7:Header><ns7:Body><ns5:SessionSetupReq><ns5:EVCCID>1C1BB56B09D6</ns5:EVCCID></ns5:SessionSetupReq></ns7:Body></ns7:V2G_Message>'
~>>> encoded_xml=encodeEXI(xml)
~>>> encoded_xml
u'809802000000000000000011D018706ED5AC275800'
```
Then, the encoded/compressed data in EXI can be pushed in the V2GTP payload as follows:
```
~>>> packet.Payload=encoded_xml
~>>> packet
<Ether  type=0x86dd |<IPv6  nh=TCP dst=fe80::3e2a:b4ff:3e5f:1a4 |<TCP  sport=6666 dport=54054 flags=PA |<V2GTP  Payload='809802000000000000000011D018706ED5AC275800' |>>>>
```
To finish, the packet can be sent to the target using Scapy's `sendp()` function.

## Further development

* Make a native Python EXI encoder/decoder -> very long task to do, or try using the C++ EXI Wrapper in Python
* Add other wrappers
* Add some pre-developed attacking functions during interception
* More docs

