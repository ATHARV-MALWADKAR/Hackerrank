#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0  # The first unserved city index
    
    while i < n:
        # Search for the furthest possible location for a plant to cover city 'i'
        # Maximum possible location is i + k - 1
        loc = min(i + k - 1, n - 1)
        
        # Look backward to find a suitable location (arr[loc] == 1)
        while loc >= i - k + 1 and loc >= 0 and arr[loc] == 0:
            loc -= 1
            
        # If no valid plant location was found within reach of city 'i'
        if loc < i - k + 1 or loc < 0:
            return -1
            
        # Place a plant at 'loc'
        plants += 1
        
        # Next unserved city is loc + k
        i = loc + k
        
    return plants

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna