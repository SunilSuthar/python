import socket

server=("localhost",9080)

s = socket.socket()

s.connect(server)

print(str(s.recv(10),"UTF-8"))

s.close()
