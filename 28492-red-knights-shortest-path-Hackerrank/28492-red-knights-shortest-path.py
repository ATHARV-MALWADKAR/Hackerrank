#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

from collections import deque

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Moves ordered strictly by priority: UL, UR, R, LR, LL, L
    moves = [
        (-2, -1, "UL"),
        (-2, 1, "UR"),
        (0, 2, "R"),
        (2, 1, "LR"),
        (2, -1, "LL"),
        (0, -2, "L")
    ]
    
    # BFS Queue stores: (row, col, path_as_list)
    queue = deque([(i_start, j_start, [])])
    visited = {(i_start, j_start)}
    
    while queue:
        r, c, path = queue.popleft()
        
        # Target reached
        if r == i_end and c == j_end:
            print(len(path))
            print(" ".join(path))
            return
            
        for dr, dc, move_name in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, path + [move_name]))
                
    # If the target is unreachable
    print("Impossible")

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna