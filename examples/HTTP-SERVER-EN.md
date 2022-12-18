# HTTP Server
This module provides a simple HTTP server that can be used to serve static files from a local folder.

## Modules used
`http.server`: used to create the HTTP server

`socketserver`: used to handle incoming connections to the server

`sys`: used to get command line arguments

`pathlib`: used to get the absolute path to the current folder

## Running the script
To use the script, make sure you have the http.server, socketserver, sys and pathlib modules installed. Then, you can run the script from the command line using the following format:
```
python script.py <port>
```

For example, to start the HTTP server on port 8080, you can use the following command:

```
python script.py 8080
```

When the server is started, it will print a message indicating the port it is listening on and will keep running until interrupted by ``CTRL + C`. If no port is specified as an argument, an error message will be displayed indicating missing parameters.