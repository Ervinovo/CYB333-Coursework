import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """
    Check whether a port is open.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

    except Exception as error:
        print(f"Error scanning port {port}: {error}")


# Get target IP from user
ip = input("Enter IP Address: ")

# Ports to scan
ports = [21, 22, 80, 443]

# Create a thread pool and scan ports concurrently
with ThreadPoolExecutor(max_workers=4) as executor:
    for port in ports:
        executor.submit(scan_port, ip, port)

print("Scan complete.")
