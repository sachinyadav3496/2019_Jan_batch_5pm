import socket

server = socket.socket()

server.bind(('localhost',12345))

server.listen(5)
client_list = []

def client_connect() : 
    c,a = server.accept()
    client_list.append(c)
    th2 = threading.Thread(target=recv,args=(c,))
    th2.start()

def recv(c) : 
    msg = c.recv(1024)
    for cl in client_list : 
        cl.send(msg)

import threading 

th1 = threading.Thread(target=client_connect,args=())
th1.start()
