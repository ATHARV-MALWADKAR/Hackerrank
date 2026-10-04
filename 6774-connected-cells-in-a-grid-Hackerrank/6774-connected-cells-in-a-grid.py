#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_region = 0
    
    # 8 directional offsets (horizontal, vertical, diagonal)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    def dfs(r, c):
        # Base cases: out of bounds or cell is 0 (unvisited/empty)
        if r < 0 or r >= n or c < 0 or c >= m or matrix[r][c] == 0:
            return 0
        
        # Mark cell as visited by setting it to 0
        matrix[r][c] = 0
        size = 1
        
        # Explore all 8 connected directions
        for dr, dc in directions:
            size += dfs(r + dr, c + dc)
            
        return size

    # Iterate through every cell in the grid
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                max_region = max(max_region, dfs(r, c))
                
    return max_region
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna