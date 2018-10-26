import socket

ip_port = ("127.0.0.1", 8888)


sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

	msg_input = input("请输入消息:")
	if msg_input == "exit":
		break
	sk.sendto(msg_input.encode(), ip_port)
sk.close()
