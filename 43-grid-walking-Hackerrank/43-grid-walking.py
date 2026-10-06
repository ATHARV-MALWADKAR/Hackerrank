#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridWalking' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY D
#

def gridWalking(m, x, D):
    MOD = 10**9 + 7
    n = len(x)
    
    # Precompute factorials and combinations nCr % MOD
    fact = [1] * (m + 1)
    inv_fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    inv_fact[m] = pow(fact[m], MOD - 2, MOD)
    for i in range(m - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    # Step 1: Calculate 1D DP for each dimension d
    # ways1d[d][s] = number of ways to take 's' steps in dimension d starting at x[d] inside boundary D[d]
    ways1d = []
    for d in range(n):
        dim_size = D[d]
        start_pos = x[d] - 1  # 0-indexed
        
        # dp[p] = ways to be at position p
        dp = [0] * dim_size
        dp[start_pos] = 1
        
        dim_ways = [0] * (m + 1)
        dim_ways[0] = 1
        
        for step in range(1, m + 1):
            next_dp = [0] * dim_size
            for p in range(dim_size):
                if p > 0:
                    next_dp[p] = (next_dp[p] + dp[p - 1]) % MOD
                if p < dim_size - 1:
                    next_dp[p] = (next_dp[p] + dp[p + 1]) % MOD
            dp = next_dp
            dim_ways[step] = sum(dp) % MOD
            
        ways1d.append(dim_ways)

    # Step 2: Combine 1D results across dimensions using multinomial combinations
    # total_dp[s] = total ways to take 's' steps across first 'i' dimensions
    total_dp = ways1d[0]
    
    for d in range(1, n):
        next_total = [0] * (m + 1)
        for s1 in range(m + 1):
            if total_dp[s1] == 0:
                continue
            for s2 in range(m + 1 - s1):
                ways = (total_dp[s1] * ways1d[d][s2]) % MOD
                ways = (ways * nCr(s1 + s2, s1)) % MOD
                next_total[s1 + s2] = (next_total[s1 + s2] + ways) % MOD
        total_dp = next_total
        
    return total_dp[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        x = list(map(int, input().rstrip().split()))

        D = list(map(int, input().rstrip().split()))

        result = gridWalking(m, x, D)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna