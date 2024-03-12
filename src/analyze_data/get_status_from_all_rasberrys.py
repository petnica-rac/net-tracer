import os
import matplotlib.pyplot as plt
from ast import literal_eval
from get_status import get_status

def call_get_status_and_plot(subdirectory_path):#12/03/2024 09:09:32
    data = get_status("2024,03,12,09,09,32", subdirectory_path + '/var/log/trace-network/ping_8.8.8.8.log')
    return data

def plot_data(all_data):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    plt.figure(figsize=(10, 6))
    
    for idx, (subdir, data) in enumerate(all_data.items()):
        if data is None:
            continue
        x = [point[0] for point in data if point is not None]
        y = [point[1] for point in data if point is not None]
        plt.scatter(x, y, color=colors[idx % len(colors)], label=subdir)
    
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Combined Plot from Subdirectories')
    plt.legend()
    plt.show()

def main(base_directory):
    all_data = {}
    for item in os.listdir(base_directory):
        subdirectory_path = os.path.join(base_directory, item)
        if os.path.isdir(subdirectory_path):
            print(f'Processing {subdirectory_path}')

            data = call_get_status_and_plot(subdirectory_path)
            all_data[item] = data
    
    plot_data(all_data)

if __name__ == "__main__":
    base_directory = 'test_data/'
    main(base_directory)
