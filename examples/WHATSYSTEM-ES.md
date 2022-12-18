# WhatSystem - Scanner de sistemas operativos.
Este script permite escanear un objetivo especificado para determinar su sistema operativo utilizando el comando ping.

## Escaneo y determinación del sistema operativo
1. La función start() ejecuta el comando ping con el objetivo especificado y busca patrones específicos en la salida para determinar el sistema operativo. Los patrones utilizados son:
* Windows Server: ttl=56
* Windows Workgroups: ttl=32
* Windows genérico: ttl=128, ttl=118, ttl=112
* Linux: ttl=64, ttl=63, ttl=255, ttl=103
* Mac: ttl=60

2. Si se encuentra un patrón, se imprime en pantalla el mensaje de que el objetivo ha sido escaneado correctamente y se indica el sistema operativo detectado.

## Ejecución del script
Para utilizar el script, asegúrate de tener los módulos sys, os, socket y datetime instalados. Luego, puedes ejecutar el script desde la línea de comandos utilizando el siguiente formato:
```
python whatsystem.py <IP_del_objetivo>
```
Por ejemplo, para escanear el objetivo `www.example.com`, puedes utilizar el siguiente comando:
```
python whatsystem.py www.example.com
```