#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    x.sort()
    n = len(x)
    i = 0
    transmitters = 0
    
    while i < n:
        # Find the location of the leftmost uncovered house
        start = x[i]
        
        # Find the furthest house to the right within range k to place the transmitter
        while i < n and x[i] <= start + k:
            i += 1
        
        # Place transmitter at x[i - 1]
        loc = x[i - 1]
        transmitters += 1
        
        # Skip all houses covered by this transmitter (range loc + k)
        while i < n and x[i] <= loc + k:
            i += 1
            
    return transmitters
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna