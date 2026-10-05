#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

import math

def chiefHopper(arr):
    energy = 0
    
    # Work backwards from the last building to the first
    for height in reversed(arr):
        # Reverse energy transition:
        # new_energy = 2 * old_energy - height
        # => old_energy = (new_energy + height) / 2
        energy = math.ceil((energy + height) / 2)
        
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna