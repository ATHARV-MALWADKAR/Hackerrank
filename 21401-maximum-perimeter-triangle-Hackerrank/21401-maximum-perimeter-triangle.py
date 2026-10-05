#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
def maximumPerimeterTriangle(sticks):
    # Sort stick lengths in non-decreasing order
    sticks.sort()
    
    # Iterate from the largest sticks backwards to find the maximal valid triangle
    for i in range(len(sticks) - 3, -1, -1):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return [sticks[i], sticks[i+1], sticks[i+2]]
            
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna