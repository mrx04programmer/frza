import paramiko
import argparse
from datetime import datetime
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GRs = '\033[1;37m'  # gray

frza = W+'frza '
ok = G+'OK '+W
err = R+'ERR '+W
inf = B+'INF '+W
def banner():
    print(G+"."*50)
    print(frza+ok+'objetivo agregado ('+O+target+W+')')
    print(frza+inf+'iniciando análisis SSH '+G+str(datetime.now()))
    print(G+"."*50)

parse = argparse.ArgumentParser()
parse.add_argument("-t", "--target",help="IP/Dominio objetivo")
parse.add_argument("-p", "--port", help="Puerto del objetivo")
parse.add_argument("-u", "--user", help="Username del objetivo")
parse.add_argument("-ps", "--password", help="Contraseña del objetivo")
parse.add_argument("-c", "--command", help="Comando a enviar")
parse = parse.parse_args()
########
target = str(parse.target)
user = str(parse.user)
passwd = str(parse.password)
p = str(parse.port)
command = str(parse.command)

client = paramiko.SSHClient()
client.set_missing_Host_key_policy(paramiko.AutoAddPolicy())
client.connect(target,port=p, username=user, password=passwd)

entrada, salida, errores = client.exec_command(command)
print (salida.read())
client.close()