import socket


def scan_port(host, port):
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(1)
            result = scanner.connect_ex((host, port))

            if result == 0:
                return True

    except socket.gaierror:
        print("Hostname could not be resolved.")
        return False

    except socket.error as error:
        print(f"Socket error: {error}")
        return False

    return False


def main():
    

    host = input(
        "Enter target host (127.0.0.1 or scanme.nmap.org): "
    ).strip()

    # Assignment restriction
    allowed_hosts = ["127.0.0.1", "localhost", "scanme.nmap.org"]

    if host not in allowed_hosts:
        print("Error: Only localhost or scanme.nmap.org may be scanned.")
        return

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if start_port < 1 or end_port > 65535:
            print("Port numbers must be between 1 and 65535.")
            return

        if start_port > end_port:
            print("Starting port must be less than ending port.")
            return

    except ValueError:
        print("Invalid port number entered.")
        return

    print(f"\nScanning {host}...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port}: OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port}: CLOSED")

    print("\nScan Complete")

    if open_ports:
        print("Open Ports Found:")
        for port in open_ports:
            print(f"- {port}")
    else:
        print("No open ports found in the specified range.")


if __name__ == "__main__":
    main()
