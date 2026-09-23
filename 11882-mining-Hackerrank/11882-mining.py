#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mining' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY mines
#

def mining(k, mines):
    n = len(mines)
    pos = [m[0] for m in mines]
    w = [m[1] for m in mines]
    
    # Precompute cost[i][j]: minimum cost to consolidate mines[i...j] to 1 pickup mine
    cost = [[0] * n for _ in range(n)]
    
    for i in range(n):
        opt = i
        left_w = w[i]
        right_w = 0
        cur_cost = 0
        
        for j in range(i + 1, n):
            right_w += w[j]
            cur_cost += w[j] * (pos[j] - pos[opt])
            
            # Shift the optimal median index rightward if right weight exceeds left weight
            while opt < j and right_w > left_w:
                dist = pos[opt + 1] - pos[opt]
                cur_cost += left_w * dist - right_w * dist
                opt += 1
                left_w += w[opt]
                right_w -= w[opt]
                
            cost[i][j] = cur_cost

    # DP Initialization
    # dp[c][j] = min cost to partition first (j+1) mines using c pickup locations
    dp = [cost[0][j] for j in range(n)]
    
    for c in range(2, k + 1):
        next_dp = [0] * n
        for j in range(n):
            if j < c:
                # If number of mines <= number of pickup locations, cost is 0
                next_dp[j] = 0
            else:
                min_val = float('inf')
                for m in range(j):
                    val = dp[m] + cost[m + 1][j]
                    if val < min_val:
                        min_val = val
                next_dp[j] = min_val
        dp = next_dp
        
    return dp[n - 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    mines = []

    for _ in range(n):
        mines.append(list(map(int, input().rstrip().split())))

    result = mining(k, mines)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna