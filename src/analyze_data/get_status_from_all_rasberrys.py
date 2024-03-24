import os

import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt

import sys
from ast import literal_eval
from get_status_ping import get_status

def call_get_status_and_plot(ip_address, subdirectory_path, start_timestamp, duration):#12/03/2024 09:09:32
    data = get_status(start_timestamp, duration, subdirectory_path + '/var/log/trace-network/ping_' + ip_address +'.log')
    return data

def plot_data(all_data):
    plt.ion()
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    plt.figure(figsize=(10, 6))
    i = 0
    for idx, (subdir, data) in enumerate(all_data.items()):
        if data is None:
            continue
        x = [point[0] for point in data if point is not None]
        y = [(point[1] + i) for point in data if point is not None]
        #plt.scatter(x, y, color=colors[idx % len(colors)], label=subdir)
        plt.plot(x, y, color=colors[idx % len(colors)], label=subdir, marker='o')
        i += 2
    
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Combined Plot from Subdirectories')
    plt.legend()

    wait = True
    while(wait):
        plt.show()
        wait = input("PRESS ENTER TO CONTINUE.")

def main(ip_address, start_timestamp, duration, base_directory):
    all_data = {}
    for item in os.listdir(base_directory):
        subdirectory_path = os.path.join(base_directory, item)
        if os.path.isdir(subdirectory_path):
            print(f'Processing {subdirectory_path}')

            data = call_get_status_and_plot(ip_address, subdirectory_path, start_timestamp, int(duration))
            all_data[item] = data
    print(all_data)
    plot_data(all_data)

if __name__ == "__main__":
    base_directory = 'test_data/'
    ip_address = sys.argv[1]
    start_timestamp = sys.argv[2] #'2024,03,12,09,09,32'
    duration = sys.argv[3]#60
    main(ip_address, start_timestamp, duration, base_directory)
