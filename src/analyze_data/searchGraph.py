import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def search(G, parent_timestamp, current_node):
    #print("curr: ",current_node)
    timestamps=[]
    unpacked = G.nodes[current_node]['data']
    
    if (parent_timestamp, 1) in unpacked:
        #print ("nadjen")
        for child in nx.descendants(G, current_node):
            search(G, parent_timestamp, child)

    elif (parent_timestamp, 0) in unpacked:
        print("Node", current_node," failed")
        print("timestamp: ",parent_timestamp)
        print("Failed child devices: ")
        # Only first layer for now
        print(nx.descendants(G, current_node))

    else:
        nerby_timestamps = [datetime.strptime(parent_timestamp, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=delta) for delta in range(-20, 21)]
        for nerby_timestamp in nerby_timestamps:
            nerby_timestamp = nerby_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            #if (nerby_timestamp, 1) in unpacked:
            #    print("found with offset")
            if(nerby_timestamp, 0) in unpacked:
                print("Node", current_node," failed")
                print("timestamp: ",parent_timestamp)
                print("Failed child devices: ")
                break
