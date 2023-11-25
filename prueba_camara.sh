#!/bin/bash

current_time=$(date +%s)

formatted_time=$(date -d   "@$current_time" "+%Y-%m-%dT%H:%M:%S%:z")

name=$(date -d "@$current_time" "+%Y_%m_%d_T_%H_%M_%S_%z")

raspistill -o "/home/david/proyecto_final/images/$name.jpg"

if [ $? -eq 0 ]; then
    echo "$formatted_time,1" >> photo.txt
else
    echo "$formatted_time,0" >> photo.txt
fi
