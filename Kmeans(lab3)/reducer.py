#!/usr/bin/env python

import sys

# Function to calculate the mean of a list of points
def mean(points):
    num_points = len(points)
    if num_points == 0:
        return None
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)
    return sum_x / num_points, sum_y / num_points

current_cluster = None
points = []

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    if '\t' in line:
        cluster_id, coordinates_str = line.split('\t', 1)
        coordinates = tuple(map(float, coordinates_str.split('\t')))
        
        if current_cluster == cluster_id:
            points.append(coordinates)
        else:
            if current_cluster:
                # Emit (clusterID, points) pair
                for point in points:
                    print('%s\t%s' % (current_cluster, '\t'.join(map(str, point))))
            current_cluster = cluster_id
            points = [coordinates]

# Output the points for the last cluster
if current_cluster:
    for point in points:
        print('%s\t%s' % (current_cluster, '\t'.join(map(str, point))))
