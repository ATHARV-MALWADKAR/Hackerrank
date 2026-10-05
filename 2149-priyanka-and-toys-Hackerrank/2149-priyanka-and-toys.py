#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#
def toys(w):
    # Sort weights in non-decreasing order
    w.sort()
    
    containers = 0
    i = 0
    n = len(w)
    
    while i < n:
        containers += 1
        # The current item is the minimum weight for this container
        min_weight = w[i]
        
        # Skip all items that fall within [min_weight, min_weight + 4]
        while i < n and w[i] <= min_weight + 4:
            i += 1
            
    return containers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna