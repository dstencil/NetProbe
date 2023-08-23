# NetProbe
MVC command line application for network analysis

### Modules:
- mac_changer (testing)
- arp_spoof (untested)
- packet_sender (untested)

# Examples of mac_changer module:

Add repo to system path
```
export PATH=$PATH:/path/to/netprobe/directory
```
get current mac address:
```
netprobe current_mac -i "Ethernet(windows)" "eth0(mac/linux)"
```

change mac address:

```
netprobe change_mac -i  "Wi-Fi" -m  ff-ff-ff-ff-ff-ff
```

restore original mac address:

```
netprobe restore_mac -i  "Wi-Fi"
```
