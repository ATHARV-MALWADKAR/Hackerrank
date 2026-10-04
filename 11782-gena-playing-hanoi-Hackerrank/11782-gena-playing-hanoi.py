#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

from collections import deque

def hanoi(posts):
    n = len(posts)
    
    # Target state: all N disks are on rod 1 (encoded as 0)
    target_state = 0
    
    # Encode initial state into a bitmask integer
    # Each disk takes 2 bits to represent its rod (0, 1, 2, or 3)
    start_state = 0
    for i in range(n):
        rod = posts[i] - 1  # 0-indexed rod numbers (0 to 3)
        start_state |= (rod << (2 * i))
        
    if start_state == target_state:
        return 0
        
    queue = deque([(start_state, 0)])
    visited = {start_state}
    
    while queue:
        state, moves = queue.popleft()
        
        # Find the top (smallest) disk on each of the 4 rods
        top_disks = [float('inf')] * 4
        for disk in range(n):
            rod = (state >> (2 * disk)) & 3
            if top_disks[rod] == float('inf'):
                top_disks[rod] = disk
                
        # Try moving the top disk from rod `from_rod` to rod `to_rod`
        for from_rod in range(4):
            disk_to_move = top_disks[from_rod]
            if disk_to_move == float('inf'):
                continue  # No disk on this rod
                
            for to_rod in range(4):
                if from_rod != to_rod and disk_to_move < top_disks[to_rod]:
                    # Create the new state by clearing old 2 bits and setting new 2 bits
                    new_state = (state & ~(3 << (2 * disk_to_move))) | (to_rod << (2 * disk_to_move))
                    
                    if new_state == target_state:
                        return moves + 1
                        
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, moves + 1))
                        
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna