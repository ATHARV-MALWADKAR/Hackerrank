#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    
    start_r, start_c = -1, -1
    
    # Locate starting position 'M'
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 'M':
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    # Helper function to find valid adjacent unvisited neighbors
    def get_valid_neighbors(r, c, visited):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] != 'X' and (nr, nc) not in visited:
                neighbors.append((nr, nc))
        return neighbors

    # DFS to find the path and count wand waves
    def dfs(r, c, wand_waves, visited):
        if matrix[r][c] == '*':
            return wand_waves
            
        visited.add((r, c))
        neighbors = get_valid_neighbors(r, c, visited)
        
        # If there are 2 or more available directions, Hermione must wave her wand
        if len(neighbors) > 1:
            wand_waves += 1

        for nr, nc in neighbors:
            res = dfs(nr, nc, wand_waves, visited)
            if res is not None:
                return res

        return None

    waves = dfs(start_r, start_c, 0, set())
    
    return "Impressed" if waves == k else "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna