#!/bin/bash

trap "kill 0" SIGINT

mkdir "/tmp/trace-network" 2> /dev/null
ping_csv_file="/usr/share/trace-network/ping_devices.csv"
traceroute_csv_file="/usr/share/trace-network/traceroute_devices.csv"
#csv_file="../../data/devices.csv"

devices=()
pids=()

sleeps=()

while IFS=' ' read -r param1 param2; do
    if [[ -n "$param1" ]]; then
        if [[ -z "$param2" ]]; then
            sleeps+=("-1")  
            devices+=("$param1")
        else
            devices+=("$param1")
            sleeps+=("$param2")
        fi
    fi
done < "$ping_csv_file"

n_devices=${#devices[@]}

for (( i=0, j=0; i<$n_devices; i++, j++ )); do
    /usr/bin/ping_device.sh ${devices[$i]} ${sleeps[$i]} &
    pids[${j}]=$!
done

devices=()
sleeps=()

while IFS=' ' read -r param1 param2; do
    if [[ -n "$param1" ]]; then
        if [[ -z "$param2" ]]; then
            sleeps+=("-1")  
            devices+=("$param1")
        else
            devices+=("$param1")
            sleeps+=("$param2")
        fi
    fi
done < "$traceroute_csv_file"

n_trace_devices=${#devices[@]}

for (( i=0, j=$n_devices; i<$n_trace_devices; i++, j++ )); do
    /usr/bin/traceroute_device.sh ${devices[$i]} ${sleeps[$i]} &
    pids[${j}]=$!
done

for pid in ${pids[*]}; do
    wait $pid
done

#trap "kill -2 $pid1 $pid2" SIGINT



