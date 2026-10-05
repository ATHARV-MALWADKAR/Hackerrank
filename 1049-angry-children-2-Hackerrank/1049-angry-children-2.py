#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryChildren' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY packets
#

def angryChildren(k, packets):
    packets.sort()
    
    # Prefix sums array to calculate subarray sums in O(1)
    # pref[i] = sum of packets[0...i-1]
    n = len(packets)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + packets[i]
        
    # Calculate unfairness sum for the first window of length k (indices 0 to k-1)
    current_unfairness = 0
    current_sum = 0
    for j in range(k):
        current_unfairness += j * packets[j] - current_sum
        current_sum += packets[j]
        
    min_unfairness = current_unfairness
    
    # Slide the window of length k across the array
    # Transitioning from window [i-1 ... i+k-2] to [i ... i+k-1]:
    # - Removing packets[i-1]
    # - Adding packets[i+k-1]
    for i in range(1, n - k + 1):
        prev_val = packets[i - 1]
        next_val = packets[i + k - 1]
        
        # Sum of elements in the previous window excluding packets[i-1]
        window_sum = pref[i + k - 1] - pref[i]
        
        # Sliding window recurrence:
        # Subtract contributions of removed element and add contributions of newly added element
        current_unfairness = (
            current_unfairness 
            - (window_sum - (k - 1) * prev_val)
            + ((k - 1) * next_val - window_sum)
        )
        
        min_unfairness = min(min_unfairness, current_unfairness)
        
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    packets = []

    for _ in range(n):
        packets_item = int(input().strip())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna