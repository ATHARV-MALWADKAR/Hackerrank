#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

import math

def minimumPasses(m, w, p, n):
    # If initial production capacity already meets target, it takes 1 pass
    if m * w >= n:
        return 1
        
    candies = 0
    passes = 0
    ans = math.ceil(n / (m * w))
    
    while passes < ans:
        # Fast-forward passes if we don't have enough candies to buy anything
        if candies < p:
            needed = math.ceil((p - candies) / (m * w))
            passes += needed
            candies += needed * (m * w)
            
        # Check if doing no more purchases gets us to target faster
        remaining = math.ceil((n - candies) / (m * w)) if n > candies else 0
        ans = min(ans, passes + remaining)
        
        if candies < p:
            continue
            
        # Spend available candies to buy workers and machines
        new_items = candies // p
        candies %= p
        
        # Balance machines and workers so that |m - w| is minimized
        diff = abs(m - w)
        if m < w:
            add_m = min(new_items, diff)
            m += add_m
            new_items -= add_m
        elif w < m:
            add_w = min(new_items, diff)
            w += add_w
            new_items -= add_w
            
        # Distribute remaining new items equally
        m += new_items // 2
        w += new_items - (new_items // 2)
        
        # Produce candies for current pass after buying
        passes += 1
        candies += m * w
        
        remaining = math.ceil((n - candies) / (m * w)) if n > candies else 0
        ans = min(ans, passes + remaining)
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna