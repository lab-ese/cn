# tcp_server.py
import socket

# 1. Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind IP and port
server_socket.bind(("127.0.0.1", 8080))

# 3. Listen for client
server_socket.listen(1)
print("TCP Server waiting...")

# 4. Accept client
conn, addr = server_socket.accept()
print("Connected to:", addr)

# 5. Receive data
data = conn.recv(1024).decode()
print("Client:", data)

# 6. Send response
conn.send("Hello from TCP Server".encode())

# 7. Close connection
conn.close()
server_socket.close()