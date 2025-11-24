import socket

client = socket.socket()
client.connect(('localhost', 9999))

with open("send.txt", "rb") as f:
    data = f.read()
    client.send(data)

client.close()
