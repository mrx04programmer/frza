#! /bin/python
# _*_ ecoding: utf-8 _*_
import sys, os
import socket
from datetime import datetime
##################################
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
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

FTP_PORT = 21
FTP_USER = 'user'
FTP_PASSWD = 'password'
FTP_DIRECTORY = '/home/mrx/Workspaces'

def banner():
    print(G+"."*50)
    print(frza+ok+'Servidor Iniciando '+G+str(datetime.now()))
    print(G+"."*50)

banner()

try:
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWD, FTP_DIRECTORY, perm='elr')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 65535)

    addr = ('', FTP_PORT)
    s = FTPServer(addr, handler)
    s.max_cons = 256
    s.max_cons_per_ip = 5
    s.serve_forever()
except OSError:
    print(frza+err+' Ejecute el script con privilegios root')
