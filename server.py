import socket

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)

conn, _ = server.accept()

with open("received.txt", "wb") as f:
    data = conn.recv(1024)
    f.write(data)

conn.close()