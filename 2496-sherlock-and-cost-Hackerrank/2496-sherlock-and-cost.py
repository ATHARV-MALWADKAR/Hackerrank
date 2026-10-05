#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    n = len(B)
    
    # low_cost tracks maximum cost ending with A[i] = 1
    # high_cost tracks maximum cost ending with A[i] = B[i]
    low_cost = 0
    high_cost = 0
    
    for i in range(1, n):
        # If A[i] is set to 1:
        # Prev A[i-1] was 1 -> |1 - 1| = 0
        # Prev A[i-1] was B[i-1] -> |1 - B[i-1]| = B[i-1] - 1
        next_low = max(low_cost, high_cost + abs(1 - B[i - 1]))
        
        # If A[i] is set to B[i]:
        # Prev A[i-1] was 1 -> |B[i] - 1| = B[i] - 1
        # Prev A[i-1] was B[i-1] -> |B[i] - B[i-1]|
        next_high = max(low_cost + abs(B[i] - 1), high_cost + abs(B[i] - B[i - 1]))
        
        low_cost, high_cost = next_low, next_high
        
    return max(low_cost, high_cost)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna