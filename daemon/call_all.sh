#!/bin/bash
sleep 10
echo "ejecutando" >> /home/david/proyecto_final/prueba_send_all.txt
./prueba_humedad_exe
python prueba_temperatura.py
. prueba_camara.sh
. send_photos.sh
python prueba_mqtt.py
