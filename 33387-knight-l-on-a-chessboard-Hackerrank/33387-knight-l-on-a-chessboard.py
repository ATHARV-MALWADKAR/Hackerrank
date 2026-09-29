#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

from collections import deque

def min_moves(n, a, b):
    # All 8 possible move directions for KnightL(a, b)
    moves = [
        (a, b), (a, -b), (-a, b), (-a, -b),
        (b, a), (b, -a), (-b, a), (-b, -a)
    ]
    
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == n - 1 and c == n - 1:
            return dist
            
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
                
    return -1

def knightlOnAChessboard(n):
    result = []
    
    for a in range(1, n):
        row = []
        for b in range(1, n):
            row.append(min_moves(n, a, b))
        result.append(row)
        
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna