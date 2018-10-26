import socket

client = socket.socket()

ip_port = ("127.0.0.1", 8888)

client.connect(ip_port)

data = client.recv(1024)

print(data.decode())

while True:
	msg_input = input("请输入消息:")
	client.send(msg_input.encode())
	if msg_input == 'exit':
		break
	data = client.recv(1024)
	print(data.decode())
