#! /bin/python
# _*_ encoding: utf-8 _*_
import sys, os
from datetime import datetime
###########


W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GRs = '\033[1;37m'  # gray

global frza, ok, err, inf
frza = W+'frza '
ok = G+'OK '+W
err = R+'ERR '+W
inf = B+'INF '+W
sh = os.system
dic = {'name': '', 'lastname': '', 'nickname': '', 'nacimiento': '', 'email': '', 'skin': '', 'gender': ''}
def banner():
    print("""
       .---.
      /_____\ 
      ( '.' )
       \_-_/_
    .-"`'V'//-.
   / ,   |// , \ 
  / /|Ll //Ll|\ \        ___ _     _   ___                          _                   
 / / |__//   | \_\      /___\ |__ (_) / _ \___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 \ \/---|[]==| / /     //  // '_ \| |/ /_\/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  \/\__/ |   \/\/     / \_//| |_) | / /_\\  __/ | | |  __/ | | (_| | || (_) | |   
   |/_   | Ll_\|      \___/ |_.__// \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
     |`^'''^'|                   |__/                                              
     |   |   |                             By Mrx04programmer
     |   |   |
     |   |   |               Información necesaria : nombre, apellido, fecha de nacimiento, email.
     |   |   |               Información extra puede ser: ocupacion, numeros, etc.
     L___l___J
      |_ | _|
     (___|___)
      ^^^ ^^^               """)
def men():
    print("""
                           ,-----.
                         /'       `\  
                        ; ----,---- ;
                        | `o- |`o-  |
                        |     |_    |             Nombre :"""+str(dic['name'])+' '+str(dic['lastname'])+"""
                        |   _____,  |             Apodo  :"""+str(dic['nickname'])+' Cumpleaños : '+str(dic['nacimiento'])+"""
                         \_       _/              Correo :"""+str(dic['email'])+' Piel : '+str(dic['skin'])+"""
                         | `-----' |              Género :"""+str(dic['gender'])+"""  
                     __.-;         ;-.__
                 _,-'    ; :     ; ;    `-._
              _,'                           `.
            ,`-,_____     \ :   : /     ____,-'-,""")
def women():
    print("""
                         .-'''---.                                     
                        .'  .-.    `.                                   
                      .'  .'  ; `.   \                                  
                     /   /    :   \   \          Nombre :"""+str(dic['name'])+' '+str(dic['lastname'])+"""
                    /   /-.___;\   ;   ;         Apodo  :"""+str(dic['nickname'])+' Cumpleaños : '+str(dic['nacimiento'])+"""             
                   /   :;--.  .-^-.:   :         Correo :"""+str(dic['email'])+' Piel : '+str(dic['skin'])+"""
                  :    ;:`   :   :               Género :"""+str(dic['gender'])+"""                
                  ;   : ;          ;   ;                                
                  :   ; :   +     /  .'                                 
                   \  ;  \  --' .:s-"                                   
                    "-:.-"`.__.-";                                      
                           :     :                                      
                           ;     :                                      
                    _..+-""._    _"t-.._                                
                 .-"    \    "  '  :    `.         """)

sh('clear')
banner()
try:
    dic['name'] = str(input(C+'Nombre >> '+W))
    dic['lastname'] = str(input(C+'Apellido >> '+W))
    dic['nickname'] = str(input(C+'Apodo >> '+W))
    dic['nacimiento'] = str(input(C+'Fecha de Nacimiento(DD/MM/AAAA)>> '+W))
    dic['email'] = str(input(C+'Email >> '+W))
    dic['skin'] = str(input(C+'Color de Piel >> '+W))
    dic['gender'] = str(input(C+'Género(Hombre/Mujer) >> '+W))
    sh('clear')
    print('*'*50)
    print('Profile : '+dic['name']+' '+dic['lastname'])
    print('*'*50)
    if(dic['gender'] == 'Mujer' or dic['gender'] == 'mujer'):
        women()
    if(dic['gender'] == 'Hombre' or dic['gender'] == 'hombre'):
        men()

except ValueError as e:
    print(frza+err+'Error ! {}'.format(e))
# except TypeError as e:
#     print(frza+err+'Error ! {}'.format(e))
