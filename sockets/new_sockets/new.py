import socket


server = socket.socket()

server.bind(('localhost',12344))

client_list = []
server.listen(5)

for var in range(5) :

    c,a = server.accept()
    print("client {}:{}".format(*a))
    client_list.append(c)


for client in client_list : 
    client.send("hello World")


