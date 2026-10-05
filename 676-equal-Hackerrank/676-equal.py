#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    min_val = min(arr)
    min_ops = float('inf')
    
    # Try baseline targets: min_val, min_val - 1, min_val - 2, min_val - 3, min_val - 4
    for target_offset in range(5):
        target = min_val - target_offset
        ops = 0
        
        for x in arr:
            diff = x - target
            # Greedy reduction using 5, 2, and 1 operations
            ops += diff // 5
            diff %= 5
            ops += diff // 2
            diff %= 2
            ops += diff
            
        min_ops = min(min_ops, ops)
        
    return min_ops

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna