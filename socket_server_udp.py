import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ("127.0.0.1", 8888)

sk.bind(ip_port)

while True:
	print("连接建立成功")
	data = sk.recv(1024)
	print(data.decode())



