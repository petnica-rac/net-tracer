import re
import matplotlib.pyplot as plt
import sys

from datetime import datetime, timedelta

def parse_ping_output(lines):
    data = []
    for line in lines:
        if 'icmp_seq' in line:
            data.append(line)
    return data

def handle_data(data, start_date, end_date, flag):
    #cur_date = datetime.strptime(data[0], '%d/%m/%Y %H:%M:%S')
    cur_date = datetime.strptime(data[0], '%d/%m/%Y %H:%M:%S')
    if not (start_date <= cur_date <= end_date):
        if (cur_date > end_date):
            flag[0] = True
        return
    
    parsed_data = parse_ping_output(data)
    if parsed_data:
        #print(cur_date, "RADI")
        return (cur_date.strftime('%Y-%m-%d %H:%M:%S'), 1)
    else:
        #print(cur_date, "NE RADI")
        return (cur_date.strftime('%Y-%m-%d %H:%M:%S'), 0)

def pattern_match(file_path, pattern, start_date, end_date):
    flag=[False]
    #return_data = []
    with open(file_path, 'r') as file:
        data = None
        for line in file:
            if flag[0]:
                return
            if re.search(pattern, line):
                if data:
                    yield handle_data(data, start_date, end_date, flag)
                data = [line.strip()]
            else:
                if data is not None:
                    data.append(line.strip())
                

def get_status(start_date_str, duration, file_path):
    #file_path = '/tmp/trace-network/ping_8.8.8.8.log'
    pattern = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}' 
    #device = sys.argv[0]
    #start_date = sys.argv[1]#datetime(2024, 3,7, 21, 20, 17)
    start_date = datetime.strptime(start_date_str, '%Y,%m,%d,%H,%M,%S')
    
    #datetime(start_date_str)
    end_date = start_date + timedelta(seconds=duration)

    points = list(pattern_match(file_path, pattern, start_date, end_date))

    if points == []:
        print("No data found for the given date")
        return None
    
    x = [point[0] for point in points if point is not None]
    y = [point[1] for point in points if point is not None]
    return points