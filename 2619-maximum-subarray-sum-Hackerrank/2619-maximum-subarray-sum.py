#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#
import bisect

def maximumSum(a, m):
    max_sum = 0
    curr_prefix = 0
    prefix_sums = []
    
    for x in a:
        curr_prefix = (curr_prefix + x) % m
        max_sum = max(max_sum, curr_prefix)
        
        # Find the smallest prefix sum that is strictly greater than curr_prefix
        idx = bisect.bisect_right(prefix_sums, curr_prefix)
        if idx < len(prefix_sums):
            max_sum = max(max_sum, (curr_prefix - prefix_sums[idx] + m) % m)
            
        # Maintain sorted order of prefix sums for binary search
        bisect.insort(prefix_sums, curr_prefix)
        
    return max_sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna