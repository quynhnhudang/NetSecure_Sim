import nmap

# Create Nmap scanner object
nm = nmap.PortScanner()

# Scan target IP
target_ip = '192.168.1.2'
nm.scan(target_ip, '1-1024')

# Print scan results
for host in nm.all_hosts():
    print(f'Host: {host} ({nm[host].hostname()})')
    for proto in nm[host].all_protocols():
        print(f'Protocol: {proto}')
        ports = nm[host][proto].keys()
        for port in ports:
            print(f'Port: {port}, State: {nm[host][proto][port]["state"]}')
