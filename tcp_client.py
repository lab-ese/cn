#tcp_client.py
import socket

c = socket.socket()
c.connect(("127.0.0.1", 8080))
print("Connected to server")

c.send("Hi".encode())
print("Server: ", c.recv(1024).decode())

c.close()
