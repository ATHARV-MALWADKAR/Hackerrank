#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kMarsh' function below.
#
# The function accepts STRING_ARRAY grid as parameter.
#

def kMarsh(grid):
    m = len(grid)
    n = len(grid[0])
    
    # up[i][j]: continuous '.' upwards from (i, j) inclusive
    up = [[0] * n for _ in range(m)]
    # left[i][j]: continuous '.' to the left from (i, j) inclusive
    left = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                up[i][j] = (up[i - 1][j] + 1) if i > 0 else 1
                left[i][j] = (left[i][j - 1] + 1) if j > 0 else 1

    max_perimeter = 0

    for r1 in range(m):
        for r2 in range(r1 + 1, m):
            h = r2 - r1
            
            # Store the valid left columns for column c
            # min_col tracks the leftmost valid column that forms a continuous horizontal top & bottom
            valid_c1 = -1
            
            for c in range(n):
                # Check if current column c can serve as the right vertical boundary
                if up[r2][c] >= h + 1:
                    if valid_c1 != -1:
                        # Maximum distance both top and bottom can extend left from c
                        max_reach = min(left[r1][c], left[r2][c])
                        min_allowed_c1 = c - max_reach + 1
                        
                        # Check if valid_c1 is within reach
                        if valid_c1 >= min_allowed_c1:
                            peri = 2 * (h + c - valid_c1)
                            if peri > max_perimeter:
                                max_perimeter = peri
                        else:
                            # Search linearly ONLY within valid bounds if valid_c1 was cut off
                            for c1 in range(min_allowed_c1, c):
                                if c1 >= valid_c1 and up[r2][c1] >= h + 1:
                                    peri = 2 * (h + c - c1)
                                    if peri > max_perimeter:
                                        max_perimeter = peri
                                    break
                    else:
                        valid_c1 = c
                
                # If there's a marsh in either row at col c, reset the tracking
                if grid[r1][c] == 'x' or grid[r2][c] == 'x':
                    valid_c1 = -1

    if max_perimeter > 0:
        print(max_perimeter)
    else:
        print("impossible")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    grid = []

    for _ in range(m):
        grid_item = input()
        grid.append(grid_item)

    kMarsh(grid)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna