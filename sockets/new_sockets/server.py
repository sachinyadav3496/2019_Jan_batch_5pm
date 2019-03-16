import socket 



server = socket.socket()

server.bind(('127.0.0.1',12345))

server.listen()

print("server is running at ip 127.0.0.1:12345")
client,addr = server.accept()

print("Client is connected at {}:{}".format(*addr))


client.send(b"Hello World")
client.send(b"HI World")
client.send(b"bye bye world")

client.close()
server.close()

print("connection Closed")
