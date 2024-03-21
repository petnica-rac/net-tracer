import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from get_route_traceroute import get_status


def main():
    # Sample traceroute logs
    traceroute_logs = get_status(20, 'test_data/traceroute.log')
                                                     

# Sample traceroute logs
traceroute_logs = [
    {"timestamp": "2024-03-17 10:00:00", "ips": ["192.168.1.1", "10.10.10.1", "10.20.30.1", "173.194.22.1"]},
    {"timestamp": "2024-03-17 10:05:00", "ips": ["192.168.1.1", "10.10.10.2", "10.20.30.2", "173.194.22.2"]},
    {"timestamp": "2024-03-17 10:10:00", "ips": ["192.168.1.1", "10.10.10.3", "10.20.30.3", "173.194.22.3"]},
]

G = nx.Graph()

# Define a starting point for node positions to make the graph layout consistent
pos = {traceroute_logs[0]['ips'][0]: (0, 0)}  # Starting node position
y_offset = 1.0  # Initial y-offset to spread out different traceroute paths

colors = plt.cm.viridis(np.linspace(0, 1, len(traceroute_logs)))  # Colors for each traceroute

for log, color in zip(traceroute_logs, colors):
    prev_ip = None
    for ip in log['ips']:
        if prev_ip is not None:
            G.add_edge(prev_ip, ip, color=color)  # Add edge with color attribute
            if ip not in pos:
                # Increment x, randomize y
                pos[ip] = (pos[prev_ip][0] + 1, pos[prev_ip][1] + np.random.uniform(-0.1, 0.1))
        else:
            if ip not in pos:
                pos[ip] = (0, y_offset)
                y_offset += 0.5  # Increase y-offset for the starting point of the next traceroute
        prev_ip = ip

# Get edge colors from the graph
edge_colors = [G[u][v]['color'] for u, v in G.edges()]

# Draw the graph
nx.draw(G, pos, edge_color=edge_colors, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold')

plt.title('Traceroute Graph Representation')
plt.axis('off')  # Turn off the axis
plt.show()
