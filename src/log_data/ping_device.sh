#!/bin/bash

device=$1

while :; do
    echo "[NEW]" >> "/tmp/trace-network/ping_"$device".log"
    date +"%d %b %Y %H:%M:%S.%N" 2>&1 >> "/tmp/trace-network/ping_"$device".log"
   #echo -e "\n" >> "/tmp/trace-network/ping_"$device".log"
    ping -c 1 $device 2>&1 >> "/tmp/trace-network/ping_"$device".log"
    if [ $? -ne 0 ]; then
        echo -e "\n"$1" device is down" >> "/tmp/trace-network/ping_"$device".log"
    fi
    #echo -e "\n" >> "/tmp/trace-network/ping_"$device".log"
    sleep 2
done