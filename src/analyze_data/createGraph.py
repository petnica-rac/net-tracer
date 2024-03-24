import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from get_status_ping import get_status
from initializeGraph_sensitive import initialize_graph_sensitive
from searchGraph import search

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
def get_data_for_node(ip_address, start_time, duration, node, database):
    data = {}
    data = get_status(start_time, duration, 'test_data/' + database + '/var/log/trace-network/ping_' + ip_address +'.log')
    return data


def tmp_test(start_time, duration, root_node, database):
    
    G = nx.DiGraph()
    nodes, edges = initialize_graph_sensitive()

    # Sample start and end time for data generation
    #start_time = datetime.now()
    #end_time = start_time + timedelta(hours=1)

    # Add nodes with data
    for ip in nodes:
        data = get_data_for_node(ip, start_time, duration, ip, database)
        filtered_data = list(filter(lambda item: item is not None, data))
        data_set = set(filtered_data)
        G.add_node(ip, data=data_set)
        # CHECK: Check if set is
        print(ip)
        print(data_set)

    G.add_edges_from(edges)

    #plot_graph(G)

    root_node_index = list(G.nodes).index(root_node)
    first_node = list(G.nodes)[root_node_index]
    timestamps = G.nodes[first_node]['data']

    for data in timestamps:
        timestamp, status = data
        #print("main: ",first_node)
        #print("timestamp: ",timestamp)
        if status:
            # Check if all nodes are reachable
            for child in nx.descendants(G, first_node):
                search(G, timestamp, child)
        else:
            # Check if all nodes are unreachable, they should be
            # Currently bug where ping is interrupted for data copy, even if ping started (but not confirmed that it works) it will return failed device
            print("Node", first_node," failed")
            print("timestamp: ",timestamp)
            print("Failed child devices: ")
            # Only first layer for now
            print(nx.descendants(G, first_node))
            return

def plot_graph(G): 
    # Works better
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    plt.show()
        
    # To be fixed
    #pos = nx.spring_layout(G)  # positions for all nodes

    #nx.draw_networkx_nodes(G, pos, node_size=700)
    #nx.draw_networkx_edges(G, pos, width=2)
    #nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    #
    #plt.axis('off')  # Turn off the axis
    #plt.show()


    

if __name__ == "__main__":
    start_time = '2024,03,12,13,13,0'
    duration = 60
    root_node = '10.11.0.1'
    database = 'raspberrypi3'
    tmp_test(start_time, duration, root_node, database)