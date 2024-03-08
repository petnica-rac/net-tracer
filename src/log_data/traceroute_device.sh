#!/bin/bash

device=$1
set_sleep=$2

if [[ $set_sleep -eq -1 ]]; then
    set_sleep=2
fi

while :; do
    date "+%d/%m/%Y %H:%M:%S" 2>&1 >> "/tmp/trace-network/traceroute_"$1".log"
    echo -e "\n" >> "/tmp/trace-network/traceroute_"$1".log"
    traceroute $device 2>&1 >> "/tmp/trace-network/traceroute_"$1".log"
    echo -e "\n" >> "/tmp/trace-network/traceroute_"$1".log"
    sleep $set_sleep
done