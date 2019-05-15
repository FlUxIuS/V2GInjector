# V2GInjector

Tool to penetrate V2G networks, monitor and inject packets to attack electric cars and charging stations.

## Dependencies

### Software 

- Python 2 (soon Python 3)
- Scapy (use Scapy for Python3 if you prefer Python3)
- Colorama for Python
- V2Gdecoder in submodules, that is already compiled and available here: https://github.com/FlUxIuS/V2Gdecoder/releases
- HomePlugPWN that is providen in dependencies

To install Python dependencies, use `pip install -r requirements.txt` (or `pip3` as needed).

Submodules can be fetched as follows:
```
git submodule sync --recursive
```

### Hardware

Any devices using Qualcomm Atheros 7k baseband. 

The tool has been tested with following devices:

* TODO

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

Then, when calling `pcap()` or `sniff()` methods as follows, EXI data are simply decoded as follows:
```
TODO
```


### Collected HPGP keys

Collected HomePlug GP keys are directly show when calling `pcap()` or `sniff()` methods as follows:
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
This can then be used to configure your PLC device's PIB as follows:
```
TODO
```
