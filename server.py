#server socket
import socket
server_socket = socket.socket()
server_socket.bind(('192.168.1.111',12345))
server_socket.listen()

client_socket,client_address = server_socket.accept()
print(f"Client {socket.gethostbyaddr(client_address[0])}")

for var in range(10) : 
    msg = input("server--> ")
    client_socket.send(msg.encode())
    m = client_socket.recv(1024).decode()
    print(f"\t\t\tclient--> {m}")
client_socket.close()
server_socket.close()
