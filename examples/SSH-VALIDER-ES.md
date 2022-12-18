# Modulo de SSH Valider
## Módulos utilizados
`paramiko`: utilizado para realizar la conexión SSH

`argparse`: utilizado para parsear argumentos de línea de comandos

## Variables y funciones
`W`, `R`, `G`, `O`, `B`, `P`, `C`, `GRs`: variables de color para la impresión en pantalla

`banner()`: imprime una bandera en la pantalla

## Procesamiento de argumentos y conexión SSH
1. Se crea un objeto parse del tipo ArgumentParser y se agregan los siguientes argumentos:

`-t` o `--target`: dirección IP o dominio del objetivo al que se desea conectar

`-p` o `--port`: puerto del objetivo al que se desea conectar

`-u` o `--user`: nombre de usuario para acceder al objetivo

`-ps` o `--password`: contraseña para acceder al objetivo

`-c` o `--command`: comando a enviar al servidor
2. Se asignan estos argumentos a variables para su uso posterior:

`target`: dirección IP/dominio del objetivo
`user`: nombre de usuario para acceder al objetivo
`passwd`: contraseña para acceder al objetivo
`p`: puerto del objetivo
`command`: comando a enviar al servidor

3. Se crea un objeto `client` del tipo `SSHClient` y se establece la política de clave del host faltante en `AutoAddPolicy` para que la clave del host se agregue automáticamente si es necesario.
Se realiza la conexión SSH al objetivo especificado utilizando el objeto `client`.

## Envío de comando y impresión de salida
1. Se envía el comando especificado al servidor utilizando el método `exec_command` del objeto `client`.

2. Se obtiene la salida del comando y se imprime en pantalla.
3. Se cierra la conexión SSH utilizando el método `close` del objeto `client`.

## Ejecución del script
Para utilizar el script, asegúrese de tener los módulos `paramiko` y `argparse` instalados. Luego, puede ejecutar el script desde la línea de comandos utilizando los siguientes argumentos:

`-t` o `--target`: dirección IP o dominio del objetivo al que se desea conectar

`-p` o `--port`: puerto del objetivo al que se desea conectar

`-u` o `--user`: nombre de usuario para acceder al objetivo

`-ps` o `--password`: contraseña para acceder al objetivo

`-c` o `--command`: comando a enviar al servidor

Por ejemplo, para conectar al objetivo `192.168.1.100` utilizando el usuario `user` y la contraseña `pass` y enviar el comando `ls -l` puede utilizar el siguiente comando:
```
python script.py -t 192.168.1.100 -u user
-ps pass -c "ls -l"
```
Cuando se conecta al objetivo y se envía el comando, el script imprimirá la salida del comando en la pantalla. Luego, cerrará la conexión SSH.