import socket

def scan_ports(target_ip, ports_list):
    print(f"[+] Starting scan on target: {target_ip}")
    for port in ports_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[!] Port {port} is OPEN!")
        s.close()

# Example usage for local testing
ports_to_scan = [21, 22, 80, 443, 8080]
target = "127.0.0.1" 
scan_ports(target, ports_to_scan)
