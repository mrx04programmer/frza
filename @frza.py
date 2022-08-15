#! /bin/python
# _*_ ecoding: utf-8 _*_
import sys, os
import socket
from datetime import datetime
###########
import requests
import argparse
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
sh = os.system
########
parse = argparse.ArgumentParser()
parse.add_argument("-u", "--url",help="Url Objetivo (ex: 127.0.0.1:8080 , google.com , http://vekatech.com)")
parse.add_argument("-a", "--agent", help="Nombre del User-Agent a enviar")
parse.add_argument("-c", "--cookie",help="Establecer cookie-string a enviar petición")
parse = parse.parse_args()
########
target = parse.url 
cookie = parse.cookie
agent = parse.agent
def banner():
    print(G+"."*50)
    print(frza+ok+'objetivo agregado ('+O+target+W+')')
    print(frza+inf+'iniciando análisis '+G+str(datetime.now()))
    print(G+"."*50)
def start():
    #cabeceras = {'cache-control': 'no-cache', 'accept': 'text/html'} 
    r = requests.post(target)
    url = r.url
    reason = r.reason
    content = r.text
    encoding = r.encoding
    code_status = r.status_code
    headers = r.headers
    print(frza+inf+O+target+W+' Status_code: ', code_status, reason)
    print(frza+inf+O+target+W+' Encoding: ', encoding)
    print(frza+inf+O+target+W+' Headers: ', headers)
    sh("curl -b '"+cookie+"' "+target)
    print(frza+ok+O+target+W+' Cookie enviada')
    if agent:
        print(frza+ok+O+target+W+' Agente enviado')
    

banner()
try:
    if parse.url and parse.cookie:
        start()
    else:
        print(frza+err+'Falta parametro URL o Cookie, por favor revisar')
except KeyboardInterrupt:
    print('\n'+frza+err+'Interrumpido por teclado')
    exit()
except socket.gaierror:
    print('\n'+frza+err+'El nombre del target no se ha podido resolver')
    exit()
# except socket.error:
#     print('\n'+frza+err+'Ejecuta el script con privilegios root.')
#     exit()
