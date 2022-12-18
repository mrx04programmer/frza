# FRZA
Repository of ZAP files to Add 
## Modules used
`sys`: Python system module

os`: Python operating system module

`socket`: Python socket module

`datetime`: module to work with Python dates and times

`requests`: module to perform HTTP requests in Python

`argparse`: module to parse command line arguments in Python

## Execution
To run the script, make sure you have the requests and argparse module installed. Then, you can run the script from the command line using the following arguments:

`-u` or `--url`: the URL of the target to which you want to send the HTTP request. It can be an IP address or a domain.

`-c` or `--cookie`: the cookie you want to send along with the HTTP request.

a` or `--agent`: the name of the User-Agent that you want to send along with the HTTP request.

For example, to send an HTTP request to the URL `google.com` with the cookie `example=123` and the User-Agent `Mozilla/5.0`, you can use the following command:
```
python script.py -u google.com -c 'example=123' -a 'Mozilla/5.0
```
When the HTTP request is sent, the script will print the URL, status code, encoding, headers and the contents of the response. If a cookie and/or User-Agent is specified, a message indicating that they have been sent will also be printed.

If an error occurs during script execution, an error message will be printed and the execution will be closed. For example, if a URL or cookie is not specified, an error message will be printed and the script will be closed. If the target name cannot be resolved, an error message will be printed and the script will be closed.