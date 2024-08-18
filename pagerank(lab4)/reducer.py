#!/usr/bin/env python

import sys
import json

def reducer():
    node_neighbors = {}
    pageranks = {}

    # Read input from mapper and populate node_neighbors dictionary
    for line in sys.stdin:
        parts = line.strip().split("\t")
        node = parts[0]
        neighbors = json.loads(parts[1])
        node_neighbors[node] = neighbors

    # Calculate initial pageranks
    num_nodes = len(node_neighbors)
    initial_pagerank = 1.0 / num_nodes
    for node in node_neighbors:
        pageranks[node] = initial_pagerank

    # Perform 10 iterations of PageRank calculation - FOR DEMO
    num_iterations = 10
    damping_factor = 0.85
    for _ in range(num_iterations):
        new_pageranks = {}
        for node in node_neighbors:
            new_pagerank = (1 - damping_factor) / num_nodes
            for neighbor in node_neighbors[node]:
                if neighbor in node_neighbors and len(node_neighbors[neighbor]) > 0:
                    new_pagerank += damping_factor * pageranks[neighbor] / len(node_neighbors[neighbor])
            new_pageranks[node] = new_pagerank
        pageranks = new_pageranks

    # Output each node along with its list of neighbors and PageRank
    for node in sorted(node_neighbors.keys()):
        pagerank = pageranks.get(node, (1 - damping_factor) / num_nodes)  # Set pagerank for dangling nodes
        print(f"{node}\t{node_neighbors.get(node, [])}\t{pagerank}")

if __name__ == "__main__":
    reducer()
