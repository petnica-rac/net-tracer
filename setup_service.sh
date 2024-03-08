#!/bin/bash

sudo cp src/log_data/trace_devices.sh /usr/bin/trace_devices.sh
sudo cp src/log_data/ping_device.sh /usr/bin/ping_device.sh
sudo cp src/log_data/traceroute_device.sh /usr/bin/traceroute_device.sh

sudo chmod +x /usr/bin/trace_devices.sh
sudo chmod +x /usr/bin/ping_device.sh
sudo chmod +x /usr/bin/traceroute_device.sh

sudo cp trace-network.service /lib/systemd/system/trace-network.service
sudo cp trace-network.service /etc/systemd/system/trace-network.service

sudo chmod 644 /etc/systemd/system/trace-network.service

sudo systemctl enable myservice