#udp_client.py
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto("Hi".encode(), ("127.0.0.1", 8080))
print("Client: ", c.recvfrom(1024)[0].decode())
