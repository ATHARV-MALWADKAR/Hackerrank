#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER r
#  3. INTEGER s
#

def twoSubsequences(x, r, s):
    MOD = 10**9 + 7
    
    # Validation checks
    if r < s or (r + s) % 2 != 0 or (r - s) % 2 != 0:
        return 0
        
    t1 = (r + s) // 2
    t2 = (r - s) // 2
    
    n = len(x)
    max_target = max(t1, t2)
    
    # dp[cnt][s]: ways to form a subsequence of count 'cnt' with sum 's'
    dp = [[0] * (max_target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for val in x:
        for cnt in range(n, 0, -1):
            for current_sum in range(max_target, val - 1, -1):
                dp[cnt][current_sum] = (dp[cnt][current_sum] + dp[cnt - 1][current_sum - val]) % MOD

    ans = 0
    for k in range(1, n + 1):
        if t1 <= max_target and t2 <= max_target:
            ways = (dp[k][t1] * dp[k][t2]) % MOD
            ans = (ans + ways) % MOD
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    x = list(map(int, input().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna