# Servidor HTTP
Este módulo proporciona un servidor HTTP simple que puede ser utilizado para servir archivos estáticos desde una carpeta local.

## Módulos utilizados
`http.server`: utilizado para crear el servidor HTTP

`socketserver`: utilizado para manejar las conexiones entrantes al servidor

`sys`: utilizado para obtener los argumentos de línea de comandos

`pathlib`: utilizado para obtener la ruta absoluta de la carpeta actual

## Ejecución del script
Para utilizar el script, asegúrate de tener los módulos http.server, socketserver, sys y pathlib instalados. Luego, puedes ejecutar el script desde la línea de comandos utilizando el siguiente formato:
```
python script.py <puerto>
```

Por ejemplo, para iniciar el servidor HTTP en el puerto 8080, puedes utilizar el siguiente comando:

```
python script.py 8080
```

Cuando se inicia el servidor, se imprimirá un mensaje indicando el puerto en el que está escuchando y se mantendrá en ejecución hasta que se interrumpa mediante `CTRL + C`. Si no se especifica un puerto como argumento, se mostrará un mensaje de error indicando la falta de parámetros.