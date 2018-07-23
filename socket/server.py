import socket

server=("localhost",9080)

s = socket.socket()

s.bind(server)
s.listen(5)
while True:
	c, addr = s.accept()
	c.send(bytes("Hello","UTF-8"))

