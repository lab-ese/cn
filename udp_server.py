# udp_server.py
import socket

# 1. Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind IP and port
server_socket.bind(("127.0.0.1", 8080))
print("UDP Server waiting...")

# 3. Receive message
data, addr = server_socket.recvfrom(1024)
print("Client:", data.decode())

# 4. Send response
server_socket.sendto("Hello from UDP Server".encode(), addr)

server_socket.close()