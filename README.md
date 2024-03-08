# Manual

# Scripts

Script trace_devices.sh reads list of all devices to ping and creates two processes for each device: 
    1. Process that does ping: ping_device.sh
    2. Process that does trace: traceroute_device.sh
    3. Process that runs ping_device and traceroute_device for all devices in csv file devices.csv

# Data
There is csv file devices that has in line IP adress of device that needs to be traced. They are stored in /usr/share/trace-network/ and called traceroute_devices.csv and ping_devices.csv. Each line contains IP adress of device and time to sleep until next ping/traceroute. Parameters are separated with whitespace. If sleep time is not provided, 2s are default.

# Setup
Run set_service.sh to setup. After that, reboot system and it will start on boot.