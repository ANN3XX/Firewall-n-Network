import subprocess
import socket
import platform

def get_firewall_status():
    try:
        output = subprocess.check_output(['netsh', 'advfirewall', 'show', 'allprofiles', 'state'])
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    system = platform.system()
    machine = platform.machine()
    processor = platform.processor()

    network_info = f"Hostname: {hostname}\nIP Address: {ip_address}\nSystem: {system}\nMachine: {machine}\nProcessor: {processor}"
    return network_info

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Fetch firewall status
firewall_status = get_firewall_status()

# Fetch network info
network_info = get_network_info()

# Combine the firewall status and network info
combined_info = f"Firewall Status:\n{firewall_status}\n\nNetwork Info:\n{network_info}"

# Write the combined info to a text file
output_file = 'system_info.txt'
write_to_file(output_file, combined_info)

print(f"System information written to {output_file}")
