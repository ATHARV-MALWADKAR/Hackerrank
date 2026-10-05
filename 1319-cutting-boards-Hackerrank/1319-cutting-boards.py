#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'boardCutting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost_y
#  2. INTEGER_ARRAY cost_x
#

def boardCutting(cost_y, cost_x):
    MOD = 10**9 + 7
    
    # Sort cut costs in descending order
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)
    
    # Track segment counts
    h_segments = 1
    v_segments = 1
    
    total_cost = 0
    i, j = 0, 0
    len_y, len_x = len(cost_y), len(cost_x)
    
    # Pick highest-cost cuts first
    while i < len_y and j < len_x:
        if cost_y[i] >= cost_x[j]:
            total_cost += cost_y[i] * h_segments
            v_segments += 1
            i += 1
        else:
            total_cost += cost_x[j] * v_segments
            h_segments += 1
            j += 1
            
    # Add remaining horizontal cuts
    while i < len_y:
        total_cost += cost_y[i] * h_segments
        i += 1
        
    # Add remaining vertical cuts
    while j < len_x:
        total_cost += cost_x[j] * v_segments
        j += 1
        
    return total_cost % MOD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna