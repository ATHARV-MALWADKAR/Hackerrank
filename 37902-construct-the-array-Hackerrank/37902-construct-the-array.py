#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    MOD = 10**9 + 7
    
    # Base cases for index 0 (1-st position, which must be 1)
    # ways_ends_1: number of valid arrays of current length ending with 1
    # ways_ends_other: number of valid arrays of current length ending with a specific value != 1
    ways_ends_1 = 1
    ways_ends_other = 0
    
    for _ in range(1, n):
        # To end with 1 at index i:
        # Previous element must be some value != 1 (there are k - 1 such choices,
        # all symmetric with ways_ends_other ways).
        next_ends_1 = (ways_ends_other * (k - 1)) % MOD
        
        # To end with a specific value v != 1 at index i:
        # Previous element can be 1 (1 choice, ways_ends_1 ways) OR
        # any other value != v, 1 (k - 2 choices, each with ways_ends_other ways).
        next_ends_other = (ways_ends_1 + ways_ends_other * (k - 2)) % MOD
        
        ways_ends_1, ways_ends_other = next_ends_1, next_ends_other
        
    # Return count for position n ending in x
    return ways_ends_1 if x == 1 else ways_ends_other

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna