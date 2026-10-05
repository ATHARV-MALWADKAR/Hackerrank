#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndMinimax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER p
#  3. INTEGER q
#

def sherlockAndMinimax(arr, p, q):
    arr.sort()
    
    # Candidates to test for M
    candidates = [p, q]
    
    # Midpoints between consecutive elements in the sorted array
    for i in range(len(arr) - 1):
        mid = (arr[i] + arr[i+1]) // 2
        if p <= mid <= q:
            candidates.append(mid)
            
    # Function to compute min |arr[i] - M| for a given M
    def get_min_dist(m):
        return min(abs(x - m) for x in arr)
        
    best_m = p
    max_min_dist = -1
    
    # Sort candidates to automatically prefer the smaller M in case of ties
    for m in sorted(set(candidates)):
        dist = get_min_dist(m)
        if dist > max_min_dist:
            max_min_dist = dist
            best_m = m
            
    return best_m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna