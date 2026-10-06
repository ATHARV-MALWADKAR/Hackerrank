#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPermutations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter

MOD = 10**9 + 7
MAXN = 2005

# Precompute factorials and powers of 2 for fast modular arithmetic
fact = [1] * MAXN
inv_fact = [1] * MAXN
pow2 = [1] * MAXN

for i in range(1, MAXN):
    fact[i] = (fact[i - 1] * i) % MOD
    pow2[i] = (pow2[i - 1] * 2) % MOD

inv_fact[MAXN - 1] = pow(fact[MAXN - 1], MOD - 2, MOD)
for i in range(MAXN - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def beautifulPermutations(arr):
    counts = Counter(arr)
    
    # D: number of elements appearing twice
    # S: number of elements appearing once
    D = sum(1 for c in counts.values() if c == 2)
    S = sum(1 for c in counts.values() if c == 1)
    
    n = len(arr)
    ans = 0
    
    # Inclusion-Exclusion Principle
    for k in range(D + 1):
        term = nCr(D, k) * fact[n - k] % MOD * pow2[k] % MOD
        if k % 2 == 1:
            ans = (ans - term) % MOD
        else:
            ans = (ans + term) % MOD
            
    # Account for initial overcounting due to duplicate pairs (2^D)
    inv_2_D = pow(pow2[D], MOD - 2, MOD)
    return (ans * inv_2_D) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = beautifulPermutations(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna