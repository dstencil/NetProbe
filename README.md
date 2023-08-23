# NetProbe
MVC command line application for network analysis

### Modules:
- mac_changer (testing)
- arp_spoof (untested)
- packet_sender (untested)

# Examples of mac_changer module:

get current mac address:
```
python netprobe.py current_mac -i "Ethernet(windows)" "eth0(mac/linux)"
```

change mac address:

```
python netprobe.py change_mac -i  "Wi-Fi" -m  ff-ff-ff-ff-ff-ff
```

restore original mac address:

```
python netprobe.py restore_mac -i  "Wi-Fi"
```
