#!/bin/bash

# $1 - time
# $2 - device

# $1 is start time and end time is $1 + 120s


start_date_string=$1

start_date="$(date "+%d/%m/%Y %H:%M:%S" -d "$start_date_string" )"
#end_date="07/03/2024 19:35:31"
# raw_end_date=$(date -d"${start_date} 120 seconds" "+%m/%d/%Y %H:%M:%S")

# end_date=$(date -d"$raw_end_date" "+%m/%d/%Y %H:%M:%S")



#awk -v c=2  start="$start_date" -v end="$end_date" '$0 ~ start {flag=1;next} $0 ~ end {print;flag=0} flag ' "/tmp/trace-network/ping_$2.log"

awk -v start="$start_date" -v end="$end_date" '
$0 ~ start {flag=1; start_found=1; next}
$0 ~ end {if (flag) end_found=1; flag=0}
flag
END {
    if (!start_found || !end_found) exit 1
}' "/tmp/trace-network/ping_$2.log"

echo $start_date
echo $end_date

return_code=$?
echo $return_code

if [[ $return_code -eq 1 ]]; then
        start_date=$(date -d"${start_date} 1 seconds" "+%m/%d/%Y %H:%M:%S")
        echo $start_date
        echo $end_date
        awk -v start="$start_date" -v end="$end_date" '
$0 ~ start {flag=1; start_found=1; next}
$0 ~ end {if (flag) end_found=1; flag=0}
flag
END {
    if (!start_found || !end_found) exit 1
}' "/tmp/trace-network/ping_$2.log"

fi