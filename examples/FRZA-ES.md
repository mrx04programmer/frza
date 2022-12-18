# FRZA
Repositorio de ficheros ZAP para Añadir 
## Módulos utilizados
`sys`: módulo de sistema de Python

`os`: módulo de sistema operativo de Python

`socket`: módulo de socket de Python

`datetime`: módulo para trabajar con fechas y horas de Python

`requests`: módulo para realizar peticiones HTTP en Python

`argparse`: módulo para parsear argumentos de línea de comandos en Python

## Ejecución
Para ejecutar el script, asegúrate de tener instalado el módulo requests y argparse. Luego, puedes ejecutar el script desde la línea de comandos utilizando los siguientes argumentos:

`-u` o `--url`: la URL del objetivo al que se desea enviar la petición HTTP. Puede ser una dirección IP o un dominio.

`-c` o `--cookie`: la cookie que se desea enviar junto con la petición HTTP.

`-a` o `--agent`: el nombre del User-Agent que se desea enviar junto con la petición HTTP.

Por ejemplo, para enviar una petición HTTP a la URL `google.com` con la cookie `example=123` y el User-Agent `Mozilla/5.0`, puedes utilizar el siguiente comando:
```
python script.py -u google.com -c 'example=123' -a 'Mozilla/5.0
```
Cuando se envía la petición HTTP, el script imprimirá la URL, el código de estado, el encoding, los headers y el contenido de la respuesta. Si se especifica una cookie y/o un User-Agent, también se imprimirá un mensaje indicando que se han enviado.

Si se produce un error durante la ejecución del script, se imprimirá un mensaje de error y se cerrará la ejecución. Por ejemplo, si no se especifica una URL o una cookie, se imprimirá un mensaje de error y se cerrará el script. Si no se puede resolver el nombre del objetivo, se imprimirá un mensaje de error y se cerrará el script.