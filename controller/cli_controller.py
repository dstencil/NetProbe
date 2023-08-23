# controller/cli_controller.py
from model.mac_manager import MacManager
from view.cli_view import CLIView
from model.arp_spoof import arp_spoof

class CLIController:
    def __init__(self):
        self.mac_manager = MacManager()
        self.arp_spoof = ARPspoofing()
        self.view = CLIView()

    def change_mac(self, options):
        if platform.system() == "Linux":
            self.mac_manager.change_mac_linux(options.interface, options.new_mac)
        elif platform.system() == "Windows":
            self.mac_manager.change_mac_windows(options.interface, options.new_mac)
        else:
            self.view.display_message("Unsupported OS")

    def current_mac(self, options):
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
        
    def arp_spoof(self, options):
        if options.target_ip and options.gateway_ip:
            arp_spoof(options.target_ip, options.gateway_ip)
        else:
            self.view.display_message("Please provide target and gateway IP addresses for ARP spoofing")
