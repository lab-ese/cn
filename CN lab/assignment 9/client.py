import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 8080))

# Send message to server
msg = "Hello Server, this is Client!"
client_socket.send(msg.encode())

# Receive reply from server
server_reply = client_socket.recv(1024).decode()
print("Message from Server:", server_reply)

# Close connection
client_socket.close()
