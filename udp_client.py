# udp_client.py
import socket

# 1. Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Send message
client_socket.sendto("Hello from UDP Client".encode(), ("127.0.0.1", 8080))

# 3. Receive response
data, addr = client_socket.recvfrom(1024)
print("Server:", data.decode())

client_socket.close()