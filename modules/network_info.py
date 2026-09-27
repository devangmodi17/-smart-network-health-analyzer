import socket

def network_information():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("\n--- NETWORK INFORMATION ---")
    print("Hostname   :", hostname)
    print("IP Address :", ip_address)