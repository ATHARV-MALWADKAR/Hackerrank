#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # 1. Maximum Subarray Sum (Kadane's Algorithm)
    max_subarray = arr[0]
    current_subarray = arr[0]
    
    for num in arr[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
        
    # 2. Maximum Subsequence Sum
    # If all numbers are non-positive, pick the maximum single element
    max_element = max(arr)
    if max_element <= 0:
        max_subsequence = max_element
    else:
        # Sum up all positive numbers
        max_subsequence = sum(x for x in arr if x > 0)
        
    return [max_subarray, max_subsequence]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna