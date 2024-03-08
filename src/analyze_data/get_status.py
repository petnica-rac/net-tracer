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

def handle_data(data, start_date, end_date):
    cur_date = datetime.strptime(data[0], '%d/%m/%Y %H:%M:%S')
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

if __name__ == '__main__':
    file_path = '/tmp/trace-network/ping_8.8.8.8.log'
    pattern = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}' 
    device = sys.argv(0)
    start_date = sys.args(1)#datetime(2024, 3,7, 21, 20, 17)
    end_date = start_date + timedelta(seconds=20)

    points = list(pattern_match(file_path, pattern, start_date, end_date))

    x = [point[0] for point in points if point is not None]
    y = [point[1] for point in points if point is not None]
    #plt.plot(x, y)
    #plt.show()