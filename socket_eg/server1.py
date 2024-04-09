import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((socket.gethostname(),4996))
server.listen(1)
print("Server is waiting for the client.")


connection,address = server.accept()
print(f"Connected with {address}")
msg = "Welcome"
msg = msg.encode('utf-8')
connection.send(msg)
complete_info =''
while True:
    request = connection.recv(1024)
    if len(request)==0:
        break
    complete_info+=request.decode('utf-8')
    print("Message from client is :",complete_info)
server.close()

