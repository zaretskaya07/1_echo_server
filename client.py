import socket

sock = socket.socket()
sock.setblocking(1)
while True:
	host = input('Введите адрес хоста или localhost : \n')
	if host=='localhost':
		host='127.0.0.1'
		break
	host_l=host.split('.')
	if (0<int(host_l[0])<255) and (0<int(host_l[1])<255) and (0<int(host_l[2])<255) and (0<int(host_l[3])<255):
		break
	else:
		print('Введен неверный формат адреса.')
while True:
	port=input('Введите номер порта от 1024 до 49151: \n')
	if 1023<int(port)<49152:
		break
	else:
		print('Неверный номер порта.')
		break
sock.connect((host, int(port)))

while True:
#кря
    data = sock.recv(1024)
    print(data.decode())

    if data.decode() == "Как Вас зовут?":
        name = input()
        sock.send(name.encode())

    if data.decode()=="Придумайте пароль:":
    	password=input()
    	if password!="":
    		sock.send(password.encode())

    if data.decode()=="Введите пароль: " or data.decode()=="Неверный пароль. Попробуйте еще раз.":
    	password=input()
    	sock.send(password.encode())
    	
    if "Добро пожаловать" in data.decode():
        break

msg = ""
while msg != 'exit':
	msg=input('Enter your message: ')
	sock.send(msg.encode())
	data = sock.recv(1024)
	print(data.decode())

sock.close()


