import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to IP and port
server_socket.bind(('localhost', 8080))

print("UDP Server is running and waiting for client message...")

# Receive message from client
data, addr = server_socket.recvfrom(1024)
print("Message from Client:", data.decode())
print("Client address:", addr)

# Send reply to client
reply = "Hello Client, message received by UDP Server!"
server_socket.sendto(reply.encode(), addr)

# Close (not mandatory for UDP, but good practice)
server_socket.close()
