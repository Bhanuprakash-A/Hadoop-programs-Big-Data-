#!/usr/bin/env python

import sys
import json

def emit_node(node, neighbors):
    neighbors_json = json.dumps(neighbors)
    print(f"{node}\t{neighbors_json}")

def mapper():
    node_neighbors = {}

    # Read input from mapper and populate node_neighbors dictionary
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) == 2:
            node, neighbor = parts
            if node not in node_neighbors:
                node_neighbors[node] = []
            node_neighbors[node].append(neighbor)
        elif len(parts) == 1:
            node = parts[0]
            if node not in node_neighbors:
                node_neighbors[node] = []  # Add the node with an empty list of neighbors

    # Output each node along with its neighbors
    for node, neighbors in sorted(node_neighbors.items()):
        emit_node(node, neighbors)

if __name__ == "__main__":
    mapper()
