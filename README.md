Mantequilla.py
===========

Pequeño script para controlar un poco lo que sucede en tu pequeña LAN.

¿Mantequilla?
De la expresión "repartir mantequilla".
Este script ejecuta y reparte mantequilla para todos los "intrusos"
Reparte tanta que si la red es muy grande y se ejecuta automaticamente cada poco tiempo,
genera mucho tráfico y puede llegar a saturar la red.

Así que el script se pone con una periocidad de 15 - 30 minutos, más o menos.

Está pensado para programar un equipo fijo ejemplo una Raspberry Pi, con una IP fija.
Esto es debido por la carga de tráfico y tiempo que puede transcurrir para finalizar el scanner.
Por defecto el script es lo más "rápido" posible. Los scanneos de los puertos no son tan completos como yo desearía.
Sólo se scanenan los puertos más comunes por nmap, scanear todos ralentiza mucho.

Esta pensado para configurar nuestro router Wifi, en el caso de que surja una alerta
De está forma nos mantiene lo más segura posible nuestra red.




