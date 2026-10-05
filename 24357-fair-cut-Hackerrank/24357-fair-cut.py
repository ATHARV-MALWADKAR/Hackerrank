#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def fairCut(k, arr):
    n = len(arr)
    arr.sort()
    
    INF = float('inf')
    # dp[j] stores the min cost using processed elements where j elements are assigned to Li
    dp = [INF] * (k + 1)
    dp[0] = 0
    
    for i in range(n):
        next_dp = [INF] * (k + 1)
        for j in range(min(i + 1, k + 1)):
            if dp[j] == INF:
                continue
            
            lu_count = i - j  # elements assigned to Lu so far
            
            # Option 1: Assign arr[i] to Li (set I)
            if j + 1 <= k:
                cost_li = arr[i] * (lu_count - ((n - k) - lu_count))
                if dp[j] + cost_li < next_dp[j + 1]:
                    next_dp[j + 1] = dp[j] + cost_li
                    
            # Option 2: Assign arr[i] to Lu (set J)
            if lu_count + 1 <= n - k:
                cost_lu = arr[i] * (j - (k - j))
                if dp[j] + cost_lu < next_dp[j]:
                    next_dp[j] = dp[j] + cost_lu
                    
        dp = next_dp
        
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna