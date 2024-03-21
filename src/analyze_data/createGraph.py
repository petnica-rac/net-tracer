import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from get_status_ping import get_status

# Function to generate sample data: Array of tuples (time, boolean status)
def generate_sample_data(start_time, end_time, interval_minutes, true_chance=0.5):
    data = []
    current_time = start_time
    while current_time <= end_time:
        status = np.random.random() < true_chance  # Randomly decide status based on true_chance
        data.append((current_time.strftime('%Y-%m-%d %H:%M:%S'), status))
        current_time += timedelta(minutes=interval_minutes)
    return data

# Get data for each device from one raspberry pi
def get_data_for_node(ip_address, start_time, duration, node):
    data = {}
    data = get_status(start_time, duration, 'test_data/raspberrypi3/var/log/trace-network/ping_' + ip_address +'.log')
    return data

def tmp_test():
    # Define nodes and edges to keep them consistent accress all graphs
    


    # Initialize a directed graph
    G = nx.DiGraph()

    # Sample start and end time for data generation
    #start_time = datetime.now()
    #end_time = start_time + timedelta(hours=1)

    start_time = '2024,03,12,09,11,47'
    duration = 60

    # Add nodes with data
    #node_data = {
    #    node:{
    #        'ip': node[1],
    #        'data': get_data_for_node(node[1], start_time, duration, node)
    #        #'data' : generate_sample_data(start_time, end_time, 15, 0.5)
    #    } for node in enumerate(nodes)
    #}

    #for ip, data in node_data.items():
    #    #print(data)
    #    G.add_node(ip, **data)
    #    print(node, data)
    for ip in nodes:
        data = get_data_for_node(ip, start_time, duration, ip)
        G.add_node(ip, data=data)

    G.add_edges_from(edges)

    #print(G.number_of_nodes())
    #print(G.number_of_edges())

    first_node = list(G.nodes)[0]
    timestamps = G.nodes[first_node]['data']

    for data in timestamps:
        if data is not None:
            timestamp, status = data
            #print(timestamp, status)
            print("main: ",first_node)
            print("timestamp: ",timestamp)
            if status:
                for child in nx.descendants(G, first_node):
                    search(G, timestamp, child)
            else:
                print("Node failed")
                print(nx.descendants(G, first_node))
                return
            

    #nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    #plt.show()

    #for node in G.nodes:
    #    print (G.nodes[node]['data'])
    #    print("IP Address:", node)
    #    print("Data List:", G.nodes[node]['data'])

def search(G, parent_timestamp, current_node):
    flag = False
    print("curr: ",current_node)
    timestamps=[]
    unpacked = G.nodes[current_node]['data']
    for data in unpacked:
        if data is not None:
            timestamp, status = data
            timestamps.append(timestamp)
        else:
            flag = True
    if not flag:
        set_timestamps = set(timestamps)
        print("debug-------------------")
        print(parent_timestamp)
        print(set_timestamps)
        print("debug-------------------")
        if parent_timestamp in set_timestamps:
            tmp = timestamps.index(timestamp)
            _,status_unpacked = data[tmp]
            if status_unpacked:
                print("Found")
            else:
                print("Node failed, but found")
                print(nx.descendants(G, current_node))
        else:
            print("Not Found")
    flag = False
    # Implement BFS that will take status for each timestamp from first node and compare it to all the others
    #for child in nx.descendants(G, current_node):

    #    search(G, child)
    #first_node_data = G.nodes[first_node]['data']
    #for node in G.nodes:
    #    if node != first_node:
    #        node_data = G.nodes[node]['data']
    #        for timestamp in first_node_data:
    #            if timestamp in node_data:
    #                if first_node_data[timestamp] != node_data[timestamp]:
    #                    print(f"Status mismatch at timestamp {timestamp} between {first_node} and {node}")
    #            else:
    #                print(f"Missing data for timestamp {timestamp} in {node}")
    #        for timestamp in node_data:
    #            if timestamp not in first_node_data:
    #                print(f"Missing data for timestamp {timestamp} in {first_node}")
    

if __name__ == "__main__":
    tmp_test()



    # Manually add edges between nodes if needed
    #G.add_edge('Node1', 'Node2')
    #G.add_edge('Node2', 'Node3')

    # Drawing the graph
    #pos = nx.spring_layout(G)  # positions for all nodes

    #nx.draw_networkx_nodes(G, pos, node_size=700)
    #nx.draw_networkx_edges(G, pos, width=2)
    #nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    #
    #plt.axis('off')  # Turn off the axis
    #plt.show()