#udp_server.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 8080))
print("UDP Server waiting...")

data, addr = s.recvfrom(1024)
print("Client: ", data.decode())

print("Sending response...")
s.sendto("Hello".encode(), addr)
