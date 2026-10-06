#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingPieces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def summingPieces(arr):
    MOD = 10**9 + 7
    n = len(arr)
    
    # Base multiplier for arr[0]
    # C_0 = (2^n - 1) % MOD
    c_i = (pow(2, n, MOD) - 1) % MOD
    
    total_sum = 0
    
    for i in range(n):
        total_sum = (total_sum + arr[i] * c_i) % MOD
        
        # Calculate C_{i+1} for the next element using recurrence relation
        if i < n - 1:
            diff = (pow(2, n - 2 - i, MOD) - pow(2, i, MOD)) % MOD
            c_i = (c_i + diff) % MOD
            
    return total_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna