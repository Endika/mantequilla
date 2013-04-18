#!/usr/bin/env python
import os
from datetime import *
import to

#Conf##################################################
REDLAN="192.168.1.0/24" #RedLAN
IPROUTER="192.168.1.1" #IP DEL ROUTER
IPSERVIDOR="192.168.1.33" #IP DEL SERVIDOR DONDE SE EJECUTA EL SCRIPT
######################################################

myMACs = [
        "AA:AA:AA:AA:AA:AA",#RouterWifi <---PLEASE LA PRIMERA ENTRADA QUE SEA LA MAC DEL ROUTER
        "BB:BB:BB:BB:BB:BB",#MyPC
        "CC:CC:CC:CC:CC:CC",#MyPhone
        ]

nameMACs = {
        "AA:AA:AA:AA:AA:AA":"RouterWifi",
        "BB:BB:BB:BB:BB:BB":"MyPC",
        "CC:CC:CC:CC:CC:CC":"MyPhone",
        }

myPorts = [
        21,22,#FTP
        23, #TELNET
        25,587,#SMTP
        80,8080, #HTTP
        443, #HTTPS
        53, #DNS
        135, #DCHP
        199,#SMUX
        139,445,902,#SAMBA
        ]
#######################################

to.registrar("Iniciando chequeo "+str(datetime.today())+"\n")
#Buscamos todas las IPs conectadas
ip=''
os.system("nmap -sP "+str(REDLAN)+" | grep -o -E '([0-9]{1,3}\.){3}[0-9]+' > IPs.tmp ")
ip=to.listar("IPs.tmp")
#Por cada IP comprobamos su MAC y sus puertos
DEFCON=0#Nivel de peligrosidad en el analisis
#detectar posible MITM
os.system("arp -a | grep "+str(IPROUTER)+" | cut -d' ' -f4 > MITM.tmp")
router=to.leer_simple("MITM.tmp")
coint=10
while len(router) < 7 and coint > 0:
        os.system("arp -a | grep "+str(IPROUTER)+" | cut -d' ' -f4 > MITM.tmp")
        router=to.leer_simple("MITM.tmp")
        coint-=1

if coint != 0 and router[0:17].upper() != myMACs[0]:
        print router
        print myMACs[0]
        print "MITM detectado!! MAC "+str(router)
        to.registrar("MITM DETECTADO MAC: "+str(router)+"\n")
        os.system("macfilter.py "+router[0:17]+"\n")
        to.mail("MITM DETECTADO MAC: "+str(router)+"\n")
        to.registrar("MAC bloqueada")
        DEFCON=3

for i in ip:
        port=''
        mac=''
        #Comprobamos si la MAC pertenece a un INTRUSO
        os.system("nmap  "+str(i)+" | grep -oiE '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}' > MACs.tmp") #<<SOLO SCANEA LOS PUERTOS COMUNES
        #La siguiente linea comentada puede sustituir a la anterior.
        #os.system("nmap  -p- "+str(i)+" | grep -oiE '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}' > MACs.tmp") #<<<<TARDA MUCHO SCANEA TODOS LOS PUERTOS
        mac=to.leer_simple("MACs.tmp")
        if i != IPSERVIDOR and not mac[0:17] in myMACs and mac != "":
                #PREMIO REGISTRAMOS A EL INTRUSO
                print "INTRUSO DETECTADO IP: "+str(i)+" y su MAC: "+str(mac)+"\n"
                to.registrar("INTRUSO DETECTADO IP: "+str(i)+" y su MAC: "+str(mac)+"\n")
                #enviar correo
                to.mail("INTRUSO DETECTADO IP: "+str(i)+" y su MAC: "+str(mac)+" ")
                #Bloqueamos MAC
                os.system("macfilter.py "+mac[0:17]+"\n")
                to.registrar("intruso bloqueado\n")
                if DEFCON<2:
                        DEFCON=2
        #muestra solo los puertos que estan usando la maquina
        os.system("nmap  "+i+" | grep -oiE '([0-9]{1,6}/)' | grep -oiE '([0-9]{1,6})' > PORTs.tmp")
        port=to.listar("PORTs.tmp")
        #comprobamos si los puertos son seguros
        for j in port:
                if not int(j) in myPorts and j != "":
                        print "Puerto no seguro"
                        #puerto no seguro Alerta
                        name="anonimo"
                        if nameMACs.has_key(mac[0:17]):
                                name=nameMACs[mac[0:17]]
                        print "IP: "+str(i)+" PORT: "+str(j)+" MAC: "+str(mac[0:17])+" Name: "+str(name)+"\n"
                        to.registrar("IP: "+str(i)+" PORT: "+str(j)+" MAC: "+str(mac[0:17])+" Name: "+str(name)+"\n")
                        to.mail("IP: "+str(i)+" PORT: "+str(j)+" MAC: "+str(mac)+" Name: "+str(name)+"\n")
                        if DEFCON<1:
                                DEFCON=1
to.registrar("DEFCON: "+str(DEFCON)+"\n")
if DEFCON == 0:
        print "Todo OK"
elif DEFCON == 1:
        print "Hay que echar un ojo, puertos desconocidos"
elif DEFCON == 2:
        print "Reiniciamos el ROUTER"
        os.system('wifiReboot.py')
elif DEFCON == 3:
        print "Reiniciamos el ROUTER"
        os.system('wifiReboot.py')
else:
        print "NO IMPLEMENTADO"
to.registrar("Chequeo finalizado con exito "+str(datetime.today())+"\n")
to.registrar("---\n")
#FIN PROGRAMA
