import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to IP and port
server_socket.bind(('localhost', 8080))

# Listen for client connections
server_socket.listen(1)
print("Server is waiting for client connection...")

# Accept client request
conn, addr = server_socket.accept()
print("Connected to client:", addr)

# Receive message from client
client_msg = conn.recv(1024).decode()
print("Message from Client:", client_msg)

# Send message to client
server_msg = "Hello Client, message received!"
conn.send(server_msg.encode())

# Close connection
conn.close()
server_socket.close()
