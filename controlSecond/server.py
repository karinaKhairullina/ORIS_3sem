import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 55000))
socket.listen(2)
print('Сервер работает ура победа')

server = []

while True:
    conn, addr = socket.accept()
    data = conn.recv(1024)
    server.append(data)
    print(server)
    print(str(data))
    conn.send(data.upper())
conn.close()




