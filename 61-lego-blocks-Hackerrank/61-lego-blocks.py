#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    MOD = 10**9 + 7
    
    # Step 1: Ways to build a single row of width w
    row_combinations = [0] * (m + 1)
    row_combinations[0] = 1
    
    for i in range(1, m + 1):
        for step in (1, 2, 3, 4):
            if i - step >= 0:
                row_combinations[i] = (row_combinations[i] + row_combinations[i - step]) % MOD
                
    # Step 2: Total walls of height n and width w (including invalid ones)
    total_walls = [pow(row_combinations[i], n, MOD) for i in range(m + 1)]
    
    # Step 3: Compute solid walls (excluding ones with vertical splits)
    solid_walls = [0] * (m + 1)
    
    for i in range(1, m + 1):
        invalid_walls = 0
        for k in range(1, i):
            invalid_walls = (invalid_walls + solid_walls[k] * total_walls[i - k]) % MOD
        
        solid_walls[i] = (total_walls[i] - invalid_walls) % MOD
        
    return solid_walls[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna