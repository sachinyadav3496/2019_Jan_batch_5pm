import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = socket.gethostbyname(socket.gethostname())
host='192.168.1.104'
port = 12345
server_socket.connect((host,port))
while True : 
    c_msg = server_socket.recv(1024).decode()
    print("\t\t\tserver->",c_msg)
    msg = input("\nclient->")
    server_socket.send(msg.encode())
    if msg.strip().lower() == 'eof' and c_msg.lower().strip() == 'eof' : 
        server_socket.send(msg.encode())
        print("Connection is closed by client")
        server_socket.close()
        break

