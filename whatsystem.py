#! /bin/python
# _*_ ecoding: utf-8 _*_
import sys, os
import socket
from datetime import datetime
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GRs = '\033[1;37m'  # gray

frza = W+'frza@whatsystem '
ok = G+'OK '+W
err = R+'ERR '+W
inf = B+'INF '+W
sh = os.system
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print(frza+err+'Falta de parametros (target)')
    exit()
def banner():
    print(G+"."*50)
    print(frza+ok+'objetivo agregado ('+O+target+W+')')
    print(frza+inf+'iniciando análisis '+G+str(datetime.now()))
    print(G+"."*50)
def start():
    ## Machines
    windows_Workgroups = sh("ping -c1 "+target+"| grep 'ttl=32' >> /dev/null")
    windows_general = sh("ping -c1 "+target+"| grep 'ttl=128' >> /dev/null")
    windows_general2 = sh("ping -c1 "+target+"| grep 'ttl=118' >> /dev/null")
    windows_general3 = sh("ping -c1 "+target+"| grep 'ttl=112' >> /dev/null")
    linux = sh("ping -c1 "+target+"| grep 'ttl=64' >> /dev/null")
    linux2 = sh("ping -c1 "+target+"| grep 'ttl=63' >> /dev/null")
    linux3 = sh("ping -c1 "+target+"| grep 'ttl=255' >> /dev/null")
    linux4 = sh("ping -c1 "+target+"| grep 'ttl=103' >> /dev/null")
    mac = sh("ping -c1 "+target+"| grep 'ttl=60' >> /dev/null")
    if windows_general == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Windows Generico')
    if windows_general2 == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Windows Generico')
    if windows_general3 == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Windows Generico')
    if windows_Workgroups == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Windows Workgroups')
    if linux == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Linux')
    if linux2 == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Linux')
    if linux3 == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Linux')
    if linux4 == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo Linux')
    if mac == 0:
        print(frza+ok+'Objetivo escaneado correctamente')
        print(frza+ok+'Sistema Operativo MacOS')
    
    
    
banner()
try:
    start()
except KeyboardInterrupt:
    print('\n'+frza+err+'Interrumpido por teclado')
    exit()
except socket.gaierror:
    print('\n'+frza+err+'El nombre del host no se ha podido resolver')
    exit()
except socket.error:
    print('\n'+frza+err+'Host No responde...')
    exit()
