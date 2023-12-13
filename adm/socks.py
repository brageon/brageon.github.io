import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
sock.bind(server_address)
sock.listen(1)
connection, client_address = sock.accept()
while True:
    data = connection.recv(1024).decode()
    print("P1: " + data)
connection.close()
sock.close()