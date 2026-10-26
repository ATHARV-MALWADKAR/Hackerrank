#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'similarPair' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#

import sys

# Increase recursion depth for deep tree structures
sys.setrecursionlimit(300000)

def similarPair(n, k, edges):
    # Build adjacency list and track in-degrees to find the root
    adj = [[] for _ in range(n + 1)]
    has_parent = [False] * (n + 1)
    
    for u, v in edges:
        adj[u].append(v)
        has_parent[v] = True
        
    root = 1
    for i in range(1, n + 1):
        if not has_parent[i]:
            root = i
            break

    # Fenwick Tree (Binary Indexed Tree) over node values 1..n
    bit = [0] * (n + 2)

    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)

    def query(idx):
        idx = min(idx, n)
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    def range_query(l, r):
        l = max(1, l)
        r = min(n, r)
        if l > r:
            return 0
        return query(r) - query(l - 1)

    ans = 0

    def dfs(u):
        nonlocal ans
        # Count ancestors v in active path such that |u - v| <= k
        ans += range_query(u - k, u + k)
        
        # Add current node to Fenwick tree before traversing children
        update(u, 1)
        
        for v in adj[u]:
            dfs(v)
            
        # Backtrack: remove current node when exiting DFS branch
        update(u, -1)

    dfs(root)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = similarPair(n, k, edges)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna