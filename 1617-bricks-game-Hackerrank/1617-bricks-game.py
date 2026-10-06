#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bricksGame' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def bricksGame(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    
    # suffix_sum[i] stores the sum of arr[i:]
    suffix_sum = 0
    
    for i in range(n - 1, -1, -1):
        suffix_sum += arr[i]
        
        # Base cases: if fewer than 3 bricks remain, take all of them
        if n - i <= 3:
            dp[i] = suffix_sum
        else:
            # Player chooses 1, 2, or 3 bricks to minimize the opponent's remaining score
            dp[i] = max(
                suffix_sum - dp[i + 1],
                suffix_sum - dp[i + 2],
                suffix_sum - dp[i + 3]
            )
            
    return dp[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna