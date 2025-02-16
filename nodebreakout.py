from collections import defaultdict
import re

def normalize_node_key(device_name):
    match = re.match(r'(N0*\d+)', device_name)
    if match:
        return 'N' + str(int(match.group(1)[1:]))  # Convert to integer to remove leading zeros
    return None

def group_devices_by_node(devices):
    nodes = defaultdict(list)
    
    for device in devices:
        node_key = normalize_node_key(device['DeviceName'])
        if node_key:
            nodes[node_key].append(device)
    
    return dict(nodes)

# Sample devices list
devices = [
    {'DeviceName': 'N01-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.1.1.1'},
    {'DeviceName': 'N01-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.1.1.2'},
    {'DeviceName': 'N001-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.1.1.3'},
    {'DeviceName': 'N03-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.3.1.1'},
    {'DeviceName': 'N03-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.3.1.2'},
    {'DeviceName': 'N003-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.3.1.3'},
    {'DeviceName': 'N15-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.15.1.1'},
    {'DeviceName': 'N15-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.15.1.2'},
    {'DeviceName': 'N015-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.15.1.3'},
    {'DeviceName': 'N25-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.25.1.1'},
    {'DeviceName': 'N25-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.25.1.1'},
    {'DeviceName': 'N25-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.25.1.1'},
    {'DeviceName': 'N29-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.29.1.1'},
    {'DeviceName': 'N29-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.29.1.2'},
    {'DeviceName': 'N029-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.29.1.3'},
    {'DeviceName': 'N69-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.69.1.1'},
    {'DeviceName': 'N69-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.69.1.2'},
    {'DeviceName': 'N069-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.69.1.3'},
    {'DeviceName': 'N114-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.114.1.1'},
    {'DeviceName': 'N114-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.114.1.2'},
    {'DeviceName': 'N0114-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.114.1.3'},
    {'DeviceName': 'N126-ROUTER01-SR1', 'DeviceType': 'Router', 'DeviceDotIP': '10.126.1.1'},
    {'DeviceName': 'N126-SWITCH02-SS1', 'DeviceType': 'Switch', 'DeviceDotIP': '10.126.1.2'},
    {'DeviceName': 'N126-SWITCH03-SS2', 'DeviceType': 'Switch', 'DeviceDotIP': '10.126.1.3'}
]

# Organize devices into nodes
nodes = group_devices_by_node(devices)

# Print result
for node, devices in nodes.items():
    print(f"{node}: {devices}\n")
