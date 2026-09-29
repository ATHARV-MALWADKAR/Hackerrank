#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

from collections import defaultdict

def gridlandMetro(n, m, k, track):
    row_tracks = defaultdict(list)
    
    # Group tracks by row
    for r, c1, c2 in track:
        row_tracks[r].append((c1, c2))
        
    occupied_cells = 0
    
    # Merge overlapping track intervals per row
    for r, intervals in row_tracks.items():
        intervals.sort(key=lambda x: x[0])
        
        merged_start, merged_end = intervals[0]
        
        for start, end in intervals[1:]:
            if start <= merged_end:
                merged_end = max(merged_end, end)
            else:
                occupied_cells += (merged_end - merged_start + 1)
                merged_start, merged_end = start, end
                
        occupied_cells += (merged_end - merged_start + 1)
        
    return (n * m) - occupied_cells
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna