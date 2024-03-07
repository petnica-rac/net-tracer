#!/bin/bash

device=$1

while :; do
    date +"%d %b %Y %H:%M:%S.%N" 2>&1 >> "/tmp/trace-network/traceroute_"$1".log"
    echo -e "\n" >> "/tmp/trace-network/traceroute_"$1".log"
    traceroute $device 2>&1 >> "/tmp/trace-network/traceroute_"$1".log"
    echo -e "\n" >> "/tmp/trace-network/traceroute_"$1".log"
    sleep 2
done