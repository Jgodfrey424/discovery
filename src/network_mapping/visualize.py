import matplotlib.pyplot as plt
from prettytable import PrettyTable

def generate_table(devices):
    table = PrettyTable(["IP Address", "MAC Address", "Manufacturer", "Type"])
    for ip, details in devices.items():
        table.add_row([ip, details.get("mac"), details.get("manufacturer"), details.get("type")])
    print(table)

def generate_topology(devices):
    plt.figure(figsize=(10, 6))
    for idx, (ip, details) in enumerate(devices.items()):
        plt.scatter(idx, 0, label=f"{ip} ({details.get('mac')})")
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3)
    plt.title("Network Topology")
    plt.show()