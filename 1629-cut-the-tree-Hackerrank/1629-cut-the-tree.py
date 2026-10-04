#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

import sys
from collections import defaultdict

def cutTheTree(data, edges):
    # Increase recursion limit for deep tree structures
    sys.setrecursionlimit(200000)
    
    n = len(data)
    total_sum = sum(data)
    
    # Build adjacency list (1-indexed nodes)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    subtree_sums = [0] * (n + 1)
    
    # Iterative Post-Order Traversal (BFS / Topological Order) to avoid recursion stack overflow
    # Root the tree at node 1
    order = []
    parent = [0] * (n + 1)
    stack = [1]
    visited = {1}
    
    while stack:
        curr = stack.pop()
        order.append(curr)
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = curr
                stack.append(neighbor)
                
    # Calculate subtree sums bottom-up
    min_diff = float('inf')
    for node in reversed(order):
        subtree_sums[node] += data[node - 1]
        if parent[node] != 0:
            subtree_sums[parent[node]] += subtree_sums[node]
            
        # The sum of the other tree formed by cutting the edge above `node`
        other_sum = total_sum - subtree_sums[node]
        diff = abs(total_sum - 2 * subtree_sums[node])
        
        # We check valid edges (all nodes except the root node 1)
        if node != 1:
            min_diff = min(min_diff, diff)
            
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna