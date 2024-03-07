#!/bin/bash

trap "kill 0" SIGINT

mkdir "/tmp/trace-network" 2> /dev/null
csv_file="/usr/share/trace-network/devices.csv"

devices=()
pids=()

while read -r line; do
    devices+=($line)
done < "$csv_file"

n_devices=${#devices[@]}

for (( i=0, j=0; i<$n_devices; i++ )); do
    /usr/bin/ping_device.sh ${devices[$i]} &
    pids[${j}]=$!
    j=$(( $j + 1 ))
    /usr/bin/traceroute_device.sh ${devices[$i]} &
    pids[${j}]=$!
    j=$(( $j + 1 ))
done

for pid in ${pids[*]}; do
    wait $pid
done

#trap "kill -2 $pid1 $pid2" SIGINT



