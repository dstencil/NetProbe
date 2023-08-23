#!/usr/bin/env python3

from model.network_explorer import NetworkExplorer
from model.arp_spoof import ARPspoofing
from model.packet_sender import send_arp_packet, send_custom_packet
import platform
import scapy
import argparse

def current_mac_command(args):
    network_explorer = NetworkExplorer()
    current_mac = network_explorer.get_current_mac(args.interface)
    if current_mac:
        print(f"Current MAC address for {args.interface}: {current_mac}")
    else:
        print(f"Unable to retrieve MAC address for {args.interface}")

def change_mac_command(args):
    network_explorer = NetworkExplorer()

    if platform.system() == "Linux":
        network_explorer.change_mac_linux(args.interface, args.new_mac)
    elif platform.system() == "Windows":
        network_explorer.change_mac_windows(args.interface, args.new_mac)
    else:
        print("Unsupported operating system")


def restore_mac_command(args):
    network_explorer = NetworkExplorer()
    network_explorer.restore_original_mac(args.interface)

def arp_spoof_command(args):
    arpspoofer = ARPSpoofer()
    arpspoofer.arp_spoof(args.target_ip, args.gateway_ip)

def packet_sender_demo():
    target_ip = "10.0.2.5"
    target_mac = "00:11:22:33:44:55"
    source_ip = "10.0.2.1"
    source_mac = "AA:BB:CC:DD:EE:FF"
    payload = "Hello, NetProbe!"

    send_arp_packet(target_ip, target_mac, source_ip, source_mac)
    send_custom_packet(target_ip, payload)

def packet_sender_command(args):
    if args.payload_demo:
        args.payload = "Hello, NetProbe!"
        packet_sender_demo(args)
    else:
        packet_sender_demo(args)

def send_custom_packet_command(args):
    send_custom_packet(args.target_ip, args.payload)


def main():
    parser = argparse.ArgumentParser(description="NetProbe: Network and Packet Exploration Tool")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Create a subparser for the 'packet_sender' subcommand
    packet_sender_parser = subparsers.add_parser("packet_sender", help="Send custom packets")
    packet_sender_parser.add_argument("-t", "--target_ip", dest="target_ip", help="Target IP address")
    packet_sender_parser.add_argument("-tm", "--target_mac", dest="target_mac", help="Target MAC address")
    packet_sender_parser.add_argument("-s", "--source_ip", dest="source_ip", help="Source IP address")
    packet_sender_parser.add_argument("-sm", "--source_mac", dest="source_mac", help="Source MAC address")
    packet_sender_parser.add_argument("-p", "--payload", dest="payload", help="Payload to send")

    # Create a subparser for the 'current_mac' subcommand
    current_mac_parser = subparsers.add_parser("current_mac", help="Display current MAC address")
    current_mac_parser.add_argument("-i", "--interface", dest="interface", help="Interface to retrieve MAC address")

    # Create a subparser for the 'change_mac' subcommand
    change_mac_parser = subparsers.add_parser("change_mac", help="Change MAC address")
    change_mac_parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address")
    change_mac_parser.add_argument("-m", "--new_mac", dest="new_mac", help="New MAC address format 00:11:22:33:44:55")

    # Create a subparser for the 'restore_mac' subcommand
    restore_mac_parser = subparsers.add_parser("restore_mac", help="Restore original MAC address")
    restore_mac_parser.add_argument("-i", "--interface", dest="interface", help="Interface to restore MAC address")


    args = parser.parse_args()

    if args.subcommand == "change_mac":
        change_mac_command(args)
    elif args.subcommand == "current_mac":
        current_mac_command(args)
    elif args.subcommand == "restore_mac":
        restore_mac_command(args)
    elif args.subcommand == "arp_spoof":
        arp_spoof_command(args)
    elif args.subcommand == "packet_sender":
        packet_sender_demo(args)  # Call packet_sender_demo for packet sending
    else:
        print("Please provide a valid subcommand")

if __name__ == "__main__":
    main()
