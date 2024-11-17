import os
from src.network_mapping.parse import parse_nmap, parse_arp_scan
from src.network_mapping.visualize import generate_table, generate_topology

def discover_devices(interface="eth0"):
    # Run Nmap to discover devices
    print("Running Nmap...")
    os.system(f"sudo nmap -sP 192.168.1.0/24 -oN nmap_results.txt")
    devices_nmap = parse_nmap("nmap_results.txt")

    # Run Arp-scan for MAC addresses
    print("Running Arp-scan...")
    os.system(f"sudo arp-scan --interface={interface} --localnet > arp_results.txt")
    devices_arp = parse_arp_scan("arp_results.txt")

    # Combine results
    all_devices = {**devices_nmap, **devices_arp}

    # Visualize results
    generate_table(all_devices)
    generate_topology(all_devices)

    return all_devices

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    discover_devices(interface)