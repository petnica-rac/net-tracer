#!/bin/bash

# Example input line
#line="[1709760444.526895] 64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=30.1 ms"

# Extract the time from within brackets
#time_inside_brackets=$(echo "$line" | grep -oP "\[\K[^\]]+")

# Export the extracted time as an environment variable
#export TIME_INSIDE_BRACKETS="$time_inside_brackets"

# Print the extracted time for demonstration
#echo "Extracted Time: $TIME_INSIDE_BRACKETS"


#timestamp=$(date +"%d %b %Y %H:%M:%S.%N")
#echo $timestamp

# The input date format: dd/mm/yyyy hh:mm:ss
input_date="01/01/2020 12:00:00"

# Convert the input date to a format that `date` command understands (yyyy-mm-dd hh:mm:ss)
formatted_date=$(date -d"${input_date}" "+%Y-%m-%d %H:%M:%S")

# Increment the date by 120 seconds
incremented_date=$(date -d"${formatted_date} 120 seconds" "+%d/%m/%Y %H:%M:%S")

echo "Original date: $input_date"
echo "Incremented date: $incremented_date"
