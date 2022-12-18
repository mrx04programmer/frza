# WhatSystem - Operating System Scanner.
This script allows you to scan a specified target to determine its operating system using the ping command.

## Scanning and determining the operating system.
1. The start() function executes the ping command with the specified target and looks for specific patterns in the output to determine the operating system. The patterns used are:
* Windows Server: ttl=56
* Windows Workgroups: ttl=32
* Generic Windows: ttl=128, ttl=118, ttl=112
* Linux: ttl=64, ttl=63, ttl=255, ttl=103
* Mac: ttl=60

2. If a pattern is found, the message that the target has been successfully scanned is printed on the screen and the detected operating system is indicated.

## Running the script
To use the script, make sure you have the sys, os, socket and datetime modules installed. Then, you can run the script from the command line using the following format:
```
python whatsystem.py <IP_of_target>
```
For example, to scan the target `www.example.com`, you can use the following command:
```
python whatsystem.py www.example.com
```