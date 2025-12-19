#tcp_server.py
import socket

s = socket.socket()
s.bind(("127.0.0.1", 8080))
s.listen(1)
print("TCP Server waiting...")

c, addr = s.accept()
print("Connected to:", addr)
msg = c.recv(1024).decode()
print("Client: ", msg)

print("Sending response...")
c.send("Hello".encode())
c.close()
