#! /bin/python3
import http.server
import socketserver
import sys
import pathlib
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
## General

pwd = (pathlib.Path().absolute())
## Execute
def banner():
    print(G+"."*50)
    print(frza+ok+'Server HTTP en la ruta :'+P+str(pwd))
    print(G+"."*50)
def start():
    port = int(sys.argv[1])
    Handler = http.server.SimpleHTTPRequestHandler # Una conexión
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(frza+inf+'Escuchando en el puerto '+str(port))
        httpd.serve_forever()
        
banner()
try:
    start()
except KeyboardInterrupt:
    print('\n'+frza+err+'Interrumpido por teclado')
    exit()
except IndexError:
    print('\n'+frza+err+'Falta de parametros')
