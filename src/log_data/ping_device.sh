#!/bin/bash

device=$1
set_sleep=$2

if [[ $set_sleep -eq -1 ]]; then
    set_sleep=2
fi

while :; do
    echo "[NEW]" >> "/tmp/trace-network/ping_"$device".log"
    date "+%d/%m/%Y %H:%M:%S" 2>&1 >> "/tmp/trace-network/ping_"$device".log"
    ping -c 1 $device 2>&1 >> "/tmp/trace-network/ping_"$device".log"
    if [ $? -ne 0 ]; then
        echo -e "\n"$1" device is down" >> "/tmp/trace-network/ping_"$device".log"
    fi
    sleep $set_sleep
done