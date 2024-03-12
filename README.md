# Manual

# Setup
Run set_service.sh to setup. After that, reboot system and it will start on boot.

# Scripts

Script trace_devices.sh reads list of all devices to ping and creates two processes for each device: 
    1. Process that does ping: ping_device.sh
    2. Process that does trace: traceroute_device.sh
    3. Process that runs ping_device and traceroute_device for all devices in csv file devices.csv

# Data
There is csv file devices that has in line IP adress of device that needs to be traced. They are stored in /usr/share/trace-network/ and called traceroute_devices.csv and ping_devices.csv. Each line contains IP adress of device and time to sleep until next ping/traceroute. Parameters are separated with whitespace. If sleep time is not provided, 2s are default.

# Analyze
Currently get_status_from_all_raberrys.py accepts 3 parameters:
    1. **ip addres** in form of string
    2. **start date time** in form of string: yyyy,mm,dd,hh,mm,ss (separated with comma)
    3. **duration** if form of string of seconds how long should be plotted from start date time

It reads directories from test_data directory and creates 0-1 range on plot for each one of them. Further it reads var/log/trace-network/ping_ip_address.log file from each one of them, where ip_address is given. 1 Represents ping working correctly and 0 is failing. If point does not exist, device was not logging.

