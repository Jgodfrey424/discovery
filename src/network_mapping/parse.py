def parse_nmap(file_path):
    devices = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Nmap scan report for" in line:
                ip = line.split()[-1]
                devices[ip] = {"type": "Unknown", "mac": None, "hostname": None}
    return devices

def parse_arp_scan(file_path):
    devices = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if ":" in line:  # MAC address format
                parts = line.split()
                mac = parts[0]
                ip = parts[1][1:-1] if "(" in parts[1] else None
                manufacturer = " ".join(parts[2:]) if len(parts) > 2 else None
                devices[ip] = {"mac": mac, "manufacturer": manufacturer, "type": "Unknown"}
    return devices