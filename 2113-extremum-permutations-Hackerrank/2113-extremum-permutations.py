#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extremumPermutations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def extremumPermutations(n, a, b):
    MOD = 10**9 + 7
    
    # 1-based indexing for conditions array
    # 0 = free, 1 = P_{i} < P_{i+1}, -1 = P_{i} > P_{i+1}
    rel = [0] * (n + 1)
    
    set_a = set(a)
    set_b = set(b)
    
    # Check for direct conflicts between set A and set B
    if set_a.intersection(set_b):
        return 0
        
    for pos in a:
        # pos is local minimum => P_{pos-1} > P_{pos} < P_{pos+1}
        # Edge relation pos-1 -> pos (decreasing)
        if rel[pos - 1] == 1:
            return 0
        rel[pos - 1] = -1
        
        # Edge relation pos -> pos+1 (increasing)
        if rel[pos] == -1:
            return 0
        rel[pos] = 1

    for pos in b:
        # pos is local maximum => P_{pos-1} < P_{pos} > P_{pos+1}
        # Edge relation pos-1 -> pos (increasing)
        if rel[pos - 1] == -1:
            return 0
        rel[pos - 1] = 1
        
        # Edge relation pos -> pos+1 (decreasing)
        if rel[pos] == 1:
            return 0
        rel[pos] = -1

    # DP initialization: dp[j] for length 1
    dp = [1]
    
    for i in range(2, n + 1):
        pref = [0] * (i)
        curr_sum = 0
        for k in range(len(dp)):
            curr_sum = (curr_sum + dp[k]) % MOD
            pref[k + 1] = curr_sum
            
        next_dp = [0] * i
        cond = rel[i - 1]  # Relation between element (i-1) and element i
        
        for j in range(1, i + 1):
            if cond == 1:
                # Increasing: P_{i-1} < P_i => sum of dp[1...j-1]
                next_dp[j - 1] = pref[j - 1]
            elif cond == -1:
                # Decreasing: P_{i-1} > P_i => sum of dp[j...i-1]
                next_dp[j - 1] = (pref[i - 1] - pref[j - 1]) % MOD
            else:
                # Unconstrained: sum of all previous dp states
                next_dp[j - 1] = pref[i - 1]
                
        dp = next_dp

    return sum(dp) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    l = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = extremumPermutations(n, a, b)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna