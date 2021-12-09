#! /bin/python3
import socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

listener.bind(('127.0.0.1', 8080))
listener.listen(0)

print("[+] Esperando por conexiones")

connection, addr = listener.accept()

print("[+] Conexion de " + str(addr))

while True:
    command = input('>>')
    connection.send(command.encode())
    result = connection.recv(1024)
    print(result)