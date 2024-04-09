import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((socket.gethostname(),4996))
msg = client.recv(1024)
msg = msg.decode('utf-8')
print(msg)

complete= ''
while True:
    msg = input("Enter your message :")
    msg = msg.encode('utf-8')
    if len(msg)==0 or msg.endswith("q"):
        break
    client.send(msg)
