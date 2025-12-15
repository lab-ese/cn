import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_addr = ('localhost', 8080)

# Send message to server
msg = "Hello Server, this is UDP Client!"
client_socket.sendto(msg.encode(), server_addr)

# Receive reply from server
data, server = client_socket.recvfrom(1024)
print("Message from Server:", data.decode())

# Close socket
client_socket.close()
