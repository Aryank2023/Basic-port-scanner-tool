import socket

ip = 'www.google.com'
portlist = [21, 22, 23, 80]

for port in portlist:
    # 1. Socket Creation 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # 2. Connection Attempt (Non-blocking check)
    result = sock.connect_ex((ip, port))

    # 3. Print the result
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    # 4. Resource cleanup
    sock.close()