  GNU nano 2.2.6                                           Fichero: wifiReboot.py

#! /usr/bin/python

import getpass
import sys
import telnetlib

#Conf############################
HOST = "192.168.1.1" #IP ROUTER
user = "admin" #USUARIO ROUTER
password = "admin" #PASS ROUTER
#################################

tn = telnetlib.Telnet(HOST)

tn.read_until("Login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("save_and_reboot\n")
tn.write("exit\n")

print tn.read_all()


