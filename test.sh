#!/bin/bash

# Example input line
#line="[1709760444.526895] 64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=30.1 ms"

# Extract the time from within brackets
#time_inside_brackets=$(echo "$line" | grep -oP "\[\K[^\]]+")

# Export the extracted time as an environment variable
#export TIME_INSIDE_BRACKETS="$time_inside_brackets"

# Print the extracted time for demonstration
#echo "Extracted Time: $TIME_INSIDE_BRACKETS"


timestamp=$(date +"%d %b %Y %H:%M:%S.%N")
echo $timestamp