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
    nodes = ['8.8.8.8', '1.1.1.1']
    edges = [('8.8.8.8', '1.1.1.1')]
    #

    # Initialize a directed graph
    G = nx.DiGraph()

    # Sample start and end time for data generation
    #start_time = datetime.now()
    #end_time = start_time + timedelta(hours=1)

    start_time = '2024,03,12,09,11,47'
    duration = 60

    # Add nodes with data
    node_data = {
        node:{
            'ip': node[1],
            'data': get_data_for_node(node[1], start_time, duration, node)
            #'data' : generate_sample_data(start_time, end_time, 15, 0.5)
        } for node in enumerate(nodes)
    }

    for node, data in node_data.items():
        G.add_node(node, data=data)
        print(node, data)
    
    G.add_edges_from(edges)

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