#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def xorAndSum(a, b):
    MOD = 10**9 + 7
    LIMIT = 314159
    
    # Reverse string representations so index matches power of 2
    a = [int(x) for x in reversed(a)]
    b = [int(x) for x in reversed(b)]
    
    len_a = len(a)
    len_b = len(b)
    
    # Maximum bit position to check
    max_k = max(len_a, len_b + LIMIT)
    
    # Prefix sums of bits in 'b' to quickly query counts of 1s
    pref_b = [0] * (len_b + 1)
    for i in range(len_b):
        pref_b[i + 1] = pref_b[i] + b[i]
        
    def count_ones_in_b(low, high):
        """Returns the number of 1s in b in index range [low, high] (0-indexed)."""
        low = max(0, low)
        high = min(len_b - 1, high)
        if low > high:
            return 0
        return pref_b[high + 1] - pref_b[low]

    total_sum = 0
    p2 = 1  # 2^k % MOD
    
    for k in range(max_k):
        bit_a = a[k] if k < len_a else 0
        
        # Shift i ranges from 0 to 314159, corresponding to b index range [k - 314159, k]
        ones = count_ones_in_b(k - LIMIT, k)
        zeros = (LIMIT + 1) - ones
        
        if bit_a == 0:
            count_ones_at_k = ones
        else:
            count_ones_at_k = zeros
            
        total_sum = (total_sum + count_ones_at_k * p2) % MOD
        p2 = (p2 * 2) % MOD

    return total_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna