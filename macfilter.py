#! /usr/bin/python

import getpass
import sys
import telnetlib

#Conf############################
HOST = "192.168.1.1" #IP ROUTER
user = "admin" #USUARIO ROUTER
password = "admin" #PASS ROUTER
#################################

if len(sys.argv) < 2:
        print "Example: macfilter.py 00:00:00:00:00:00 [option]"a
        print "--add (default option)"
        print "--remove"
        sys.exit(0)

MAC = sys.argv[1]
ORDER = "--add"
if len(sys.argv) > 2:
        if sys.argv[2] == '--remove':
                ORDER = '--remove'

tn = telnetlib.Telnet(HOST)

tn.read_until("Login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("wlan macfilter --mode deny\n")
if len(ORDER)>2:
        tn.write("wlan macfilter " + ORDER + " " + MAC.lower() +"\n")
else:
        tn.write("wlan macfilter --add " + MAC.lower() +"\n")
        print "wlan macfilter --add " + MAC.lower() +"\n"
tn.write("exit\n")

print tn.read_all()
