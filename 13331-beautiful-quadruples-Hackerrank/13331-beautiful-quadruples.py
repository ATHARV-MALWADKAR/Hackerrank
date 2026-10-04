#!/bin/python3

import os
import sys

#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    # Sort limits so that a <= b <= c <= d
    limits = sorted([a, b, c, d])
    a, b, c, d = limits[0], limits[1], limits[2], limits[3]
    
    # Maximum possible XOR value for numbers up to 3000 is < 4096 (2^12)
    max_xor = 4096
    
    # cnt[val]: Number of pairs (w, x) with w <= x such that w ^ x == val
    cnt = [0] * max_xor
    
    # total_pairs: Total number of valid pairs (w, x) with w <= x for current x limit
    total_pairs = 0
    
    # Precompute all valid pairs (w, x) with 1 <= w <= x <= b
    # We will build `cnt` dynamically as x increases up to c
    total_quads = 0
    
    # Store counts of pairs (w, x) for x from 1 to b
    # To efficiently add pairs (w, x) as x increases up to b
    # First, pre-populate cnt for all w <= x where x <= b
    # Actually, we can iterate y from 1 to c, and z from y to d
    # For a fixed y, we consider all pairs (w, x) where x <= y and x <= b, w <= a
    
    # Pre-calculate counts of (w, x) pairs for x up to b
    # cnt[val] will hold the count of pairs (w, x) such that w ^ x == val
    
    # To optimize: accumulate total pairs (w, x) as x increases
    # B_cnt[x][val] is not strictly necessary if we accumulate state
    
    # Create frequency map for (w, x) pairs
    # B_pairs[x] stores all (w, x) pairs
    
    # Let's count pairs (w, x) where 1 <= w <= min(a, x) and 1 <= x <= b
    # We can precompute the total count of valid (w, x) pairs for x <= y
    
    # Let's compute for each x from 1 to b the contributions to cnt
    # For a given y (1 to c), all pairs (w, x) with 1 <= w <= min(a, x) and 1 <= x <= min(b, y) are valid.
    
    # Step 1: Pre-generate all (w, x) pairs and organize them by x
    # Since x goes up to b:
    x_pairs = [[] for _ in range(b + 1)]
    for w in range(1, a + 1):
        for x in range(w, b + 1):
            x_pairs[x].append(w ^ x)
            
    # Step 2: Iterate y from 1 to c and z from y to d
    # As y increases, we include all new pairs (w, x) where x = y (if y <= b)
    ans = 0
    total_wx_pairs = 0
    
    for y in range(1, c + 1):
        # Add all pairs (w, x) where x == y
        if y <= b:
            for xor_val in x_pairs[y]:
                cnt[xor_val] += 1
                total_wx_pairs += 1
                
        # Now for this y, pair it with all z where y <= z <= d
        for z in range(y, d + 1):
            yz_xor = y ^ z
            # Total valid quadruples (w, x, y, z) with w^x^y^z != 0
            # is (Total valid (w, x) pairs for x <= y) - (count of (w, x) pairs with w^x == y^z)
            ans += (total_wx_pairs - cnt[yz_xor])
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna