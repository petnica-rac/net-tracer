import csv
import get_status
from datetime import datetime, timedelta

file_path = '/tmp/trace-network/ping_8.8.8.8.log'
pattern = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}' 


with open('../../data/devices.csv', 'r') as file:
    devices = []
    reader = csv.reader(file)
    for row in reader:
        if row ==[]:
            continue
        devices.append(row)
        print(row)

for device in devices:
    start_date = datetime(2024, 3,7, 21, 20, 17)
    end_date = start_date + timedelta(seconds=20)
    print(list(get_status.pattern_match(device, pattern, start_date, end_date)))