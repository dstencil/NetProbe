# model/mac_manager.py
import subprocess
import platform
import re
import scapy

class MacManager:
    def __init__(self):
        self.original_mac = None
    def get_current_mac(self, interface):
        if not interface:
            return None
        
        result = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8")
        
        # Search for the MAC address in the output
        mac_address_search = re.search(r"Physical Address[\. ]+: ([\w\-:]+)", result)
        
        if mac_address_search:
            return mac_address_search.group(1)
        else:
            return None    
    def change_mac_linux(self, interface, new_mac):
        if not self.original_mac:
            self.original_mac = self.get_current_mac(interface)
        print(f"Changing mac address for {interface} to {new_mac} for Linux OS")
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
        print("MAC address changed successfully on Linux.")
    
    def change_mac_windows(self, interface, new_mac):
        if not self.original_mac:
            self.original_mac = self.get_current_mac(interface)
        print(f"Changing MAC address for {interface} to {new_mac} on Windows...")
        subprocess.call(["reg", "add", f"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\{interface}\\Ndi\\Params\\NetworkAddress", "/v", "DefaultValue", "/d", new_mac, "/f"])
        print("MAC address changed successfully on Windows.")
   
    def restore_original_mac(self, interface):
        if self.original_mac:
            self.change_mac(interface, self.original_mac)
            self.original_mac = None
            print("Restored original MAC address.")
        else:
            print("No original MAC address stored.")

