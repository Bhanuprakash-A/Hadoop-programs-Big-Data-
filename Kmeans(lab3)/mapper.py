#!/usr/bin/env python

import sys

# Function to calculate the distance between two points
def euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# Initialize centroids
centroids = []

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    coordinates = line.split()
    point = tuple(map(float, coordinates))

    if not centroids:
        centroids = [point]
    elif len(centroids) == 1:
        centroids.append(point)

    nearest_centroid_id = None
    min_distance = float('inf')

    for centroid_id, centroid in enumerate(centroids):
        distance = euclidean_distance(point, centroid)
        if distance < min_distance:
            min_distance = distance
            nearest_centroid_id = centroid_id

    # Emit (centroidID, point) pair
    print('%d\t%s' % (nearest_centroid_id, '\t'.join(coordinates)))