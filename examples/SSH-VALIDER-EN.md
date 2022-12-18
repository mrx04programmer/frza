## SSH Valider module
## Modules used
`paramiko`: used to perform SSH connection

`argparse`: used to parse command line arguments

## Variables and functions
`W`, `R`, `G`, `O`, `B`, `P`, `C`, `GRs`: color variables for printing on the screen

`banner()`: print a flag on the screen

## Argument processing and SSH connection
1. A parse object of type ArgumentParser is created and the following arguments are added:

`-t` or `--target`: IP address or domain of the target you want to connect to.

`-p` or `--port`: port of the target to connect to

`-u` or `--user`: user name to access the target

`-ps` or `--password`: password to access the target

`-c` or `--command`: command to be sent to the server.
2. These arguments are assigned to variables for later use:

`target`: IP address/domain of the target.
`user`: user name to access the target
`passwd`: password to access the target
p`: port of the target
`command`: command to send to the server

A `client` object of type `SSHClient` is created and the missing host key policy is set in `AutoAddPolicy` so that the host key is automatically added if necessary.
SSH connection is made to the specified target using the `client` object.

## Sending command and printing output
1. The specified command is sent to the server using the `exec_command` method of the `client` object.

2. The output of the command is obtained and printed on the screen.
Close the SSH connection using the `close` method of the `client` object.

## Executing the script
To use the script, make sure you have the `paramiko` and `argparse` modules installed. Then, you can run the script from the command line using the following arguments:

`-t` or `--target`: IP address or domain of the target you want to connect to.

`-p` or `--port`: port of the target you want to connect to

`-u` or `--user`: user name to access the target

`-ps` or `--password`: password to access the target

`-c` or `--command`: command to send to the server

For example, to connect to the target `192.168.1.100` using the user `user` and password `pass` and send the command `ls -l` you can use the following command:
```
python script.py -t 192.168.1.100 -u user
-ps pass -c "ls -l"
```
When connecting to the target and sending the command, the script will print the output of the command on the screen. It will then close the SSH connection.