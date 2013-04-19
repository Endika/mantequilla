#!/usr/bin/env python
#INICIO LIBRERIA PRINCIPAL

import os
from datetime import *
import smtplib
from email.mime.text import MIMEText
import string
from random import choice

#Config#############################
SMTP="smtp.servidor.es" #TU SERVIDOR SMTP
SMTPPORT=25 #PUERTO A USAR
EMAILDESTINO="destino@destino.com" #CORREO PARA ENVIAR LA ALERTA
EMAILORIGEN="origen@origen.com" #CORREO DESDE DONDE SE ENVIA LA ALERTA
EMAILPASS="aaaaaaaaaaaaaaaaaa" #CLAVE DEL CORREO ORIGEN
ASUNTO="Alerta Wifi" #ASUNTO DEL CORREO ALERTA
#####################################

def mail(mensaje):
        global SMTP,SMTPPORT,EMAILORIGEN,EMAILDESTINO,EMAILPASS,ASUNTO
        mailServer = smtplib.SMTP(SMTP,SMTPPORT)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(EMAILORIGEN,EMAILPASS)
        mensaje = MIMEText(str(mensaje))
        mensaje['From']=EMAILORIGEN
        mensaje['To']=EMAILDESTINO
        mensaje['Subject']=ASUNTO
        mailServer.sendmail(EMAILORIGEN,EMAILDESTINO,mensaje.as_string())
        mailServer.close()

def registrar(texto):
        fm = open("ALERTAS","a")
        fm.write(texto)
        fm.close()

def leer(fichero):
        contenido=''
        f = open(fichero, "r")
        while True:
                linea = f.readline()
                contenido = contenido + ' ' + linea
                if not linea: break
        f.close()
        os.system("rm "+fichero)
        return contenido


def leer_simple(fichero):
        contenido=''
        f = open(fichero, "r")
        while True:
                linea = f.readline()
                if not linea: break
                contenido = linea
        f.close()
        os.system("rm "+fichero)
        return contenido

def listar(fichero):
        contenido=leer(fichero)
        contenido=contenido.split()
        return contenido
        
def newPass(n):
    return ''.join([choice(string.letters + string.digits) for i in range(n)])

#FIN LIBRERIA PRINCIPAL
