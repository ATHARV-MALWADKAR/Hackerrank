#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayMerging' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY m as parameter.
#

import sys

def arrayMerging(m):
    MOD = 10**9 + 7
    n = len(m)
    
    # Precompute factorials and inverses for P(j, k)
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    # Precompute P[j][k] = P(j, k) = j! / (j-k)! to avoid function call overhead
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(n + 1):
        P[j][0] = 1
        for k in range(1, j + 1):
            P[j][k] = (fact[j] * inv_fact[j - k]) % MOD

    # max_len[i]: max contiguous increasing subarray starting at index i
    max_len = [1] * n
    for i in range(n - 2, -1, -1):
        if m[i] < m[i + 1]:
            max_len[i] = max_len[i + 1] + 1

    # dp[i][j]: valid ways for prefix m[0...i-1] with last block length j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        max_l = max_len[i]
        dp_i = dp[i]
        
        for j in range(i + 1):
            val = dp_i[j]
            if not val:
                continue
            
            limit = max_l if j == 0 else (j if j < max_l else max_l)
            P_j = P[j] if j > 0 else None
            
            for len_k in range(1, limit + 1):
                ways = P_j[len_k] if P_j else 1
                next_i = i + len_k
                dp[next_i][len_k] = (dp[next_i][len_k] + val * ways) % MOD

    return sum(dp[n]) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m_count = int(input().strip())

    m = list(map(int, input().rstrip().split()))

    result = arrayMerging(m)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna