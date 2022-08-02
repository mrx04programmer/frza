# Frza - Files Repository ZAP Adding (Spanish)
> Author: Mrx04programmer

### Lista de Herramientas
- WhatSystem : Encuentra el Sistema Operativo (OS) de un dispositivo en especifico y silenciosamente.
- HttpServer : La idea es utilizar un servidor Http tanto para el lado del desarrollo web como prueba de penetración por medio de HoneyPots.
- @Frza : El proyecto como tal que busca testing y attack en tokens en usuarios de cualquier plataforma según sus cookies (CookiesAttackRequest).
- ObjGenerator : Crear objetos en texto organizadamente para sus usos personales
- ServerFTP : Igual que el servidor Http busca tener comunicación entre dispositivos y sus diferentes pruebas.
- SSH Valider : Encuentra si un dispositivo tiene conexión de SSH y envia un comando al mismo, realizando así, automatización de comandos en SSH.

### Instalación
Para su instalación se requiere tener python3.8 instalado e instalar los requerimientos para uso de sus modulos en el proyecto. Para ello ejecutar:
- Instalar python: 

        $ sudo apt-get install python
- Instalar requerimientos:

        $ sudo python3.8 -m pip install requirements.txt
### ¿Como funciona?
![Funcionamiento](https://raw.githubusercontent.com/mrx04programmer/frza/main/what.png)
El software es iniciado en un area local, la cookie a utilizar debe ser anteriormente conseguida, FRZA conectará la cookie obtenida con un Agente de Usuario(Agent-User) que es utilizado en los navegadores para identificar que tipo de dispositivo esta ingresando al sitio web. <br>
El Agent-User puede ser modificado al enviar la petición, esta petición con la cookie es enviada al servidor especificado, luego este conectara a su base de datos encontrando el token que coincide con esa cookie temporal.
