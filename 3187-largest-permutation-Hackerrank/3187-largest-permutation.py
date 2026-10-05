#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    # Store the current index of each number for O(1) lookups
    pos = {val: i for i, val in enumerate(arr)}
    
    for i in range(n):
        if k == 0:
            break
            
        # The expected maximum number for position i
        expected = n - i
        
        # If the element at position i is not the expected maximum
        if arr[i] != expected:
            # Get the index of the expected element
            curr_pos = pos[expected]
            
            # Update the position map for the swapped values
            pos[arr[i]] = curr_pos
            pos[expected] = i
            
            # Swap the values in the array
            arr[i], arr[curr_pos] = arr[curr_pos], arr[i]
            
            # Decrement remaining allowed swaps
            k -= 1
            
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna