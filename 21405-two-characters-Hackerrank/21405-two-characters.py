#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from itertools import combinations

def alternate(s):
    unique_chars = list(set(s))
    max_len = 0
    
    # Try all pairs of distinct characters
    for c1, c2 in combinations(unique_chars, 2):
        # Filter string to contain only current pair
        filtered = [c for c in s if c == c1 or c == c2]
        
        # Check if characters alternate properly
        is_valid = True
        for i in range(len(filtered) - 1):
            if filtered[i] == filtered[i + 1]:
                is_valid = False
                break
                
        if is_valid:
            max_len = max(max_len, len(filtered))
            
    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna