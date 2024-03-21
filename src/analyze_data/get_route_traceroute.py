import re
import matplotlib.pyplot as plt
import sys

from datetime import datetime, timedelta

def parse_ping_output(lines):
    print ("STA?")
    data = []
    for line in lines:
        #analyze log from bash traceroute command and for each line get devece it went to so it can be plotted
        match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        if match:
            device = match.group()
            data.append(device)
            print (device)
    print ("huh?")
    return data

def handle_data(data, start_date, end_date):
    print ("ide")
    cur_date = datetime.strptime(data[0], '%d/%m/%Y %H:%M:%S')
    print (start_date)
    print (cur_date)
    print (end_date)
    if not (start_date <= cur_date <= end_date):
        return
    
    parsed_data = parse_ping_output(data)
    if parsed_data:
        print(cur_date, "RADI")
        return cur_date, 1
    else:
        print(cur_date, "NE RADI")
        return cur_date, 0

def pattern_match(file_path, pattern, start_date, end_date):
    with open(file_path, 'r') as file:
        data = None
        for line in file:
            if re.search(pattern, line):
                if data:
                    yield handle_data(data, start_date, end_date)
                data = [line.strip()]
            else:
                if data is not None:
                    data.append(line.strip())

#def get_status(start_date_str, duration, file_path):
def get_status(duration, file_path):
    #file_path = '/tmp/trace-network/ping_8.8.8.8.log'
    pattern = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}' 
    #device = sys.argv[0]
    #start_date = sys.argv[1]
    start_date = datetime(2024, 3,12, 9, 9, 7)
    #start_date = datetime.strptime(start_date_str, '%Y,%m,%d,%H,%M,%S')
    #datetime(start_date_str)
    end_date = start_date + timedelta(seconds=duration)

    points = list(pattern_match(file_path, pattern, start_date, end_date))

    if points == []:
        print("No data found for the given date")
        return None
    
    x = [point[0] for point in points if point is not None]
    y = [point[1] for point in points if point is not None]
    # Pack points and timestamp so it has this format {"timestamp": "2024-03-17 10:00:00", "ips": ["192.168.1.1", "10.10.10.1", "10.20.30.1", "173.194.22.1"]},
    # Pack points and timestamp so it has this format {"timestamp": "2024-03-17 10:00:00", "ips": ["192.168.1.1", "10.10.10.1", "10.20.30.1", "173.194.22.1"]}
    # = {"timestamp": str(cur_date), "ips": parsed_data}
    return points

def main(duration, base_directory):
    get_status(duration, base_directory)

if __name__ == "__main__":
    base_directory = '../../test_data/traceroute.log'
    #ip_address = sys.argv[1]
    #start_timestamp = sys.argv[2] #'2024,03,12,09,09,32'
    #duration = sys.argv[3]#60
    duration = 10
    print("hdhdhdh")
    main(duration, base_directory)
    