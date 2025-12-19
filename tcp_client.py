# tcp_client.py
import socket

# 1. Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to server
client_socket.connect(("127.0.0.1", 8080))

# 3. Send message
client_socket.send("Hello from TCP Client".encode())

# 4. Receive response
data = client_socket.recv(1024).decode()
print("Server:", data)

# 5. Close socket
client_socket.close()