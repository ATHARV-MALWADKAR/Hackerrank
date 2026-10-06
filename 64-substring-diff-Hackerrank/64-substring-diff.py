#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substringDiff' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s1
#  3. STRING s2
#

def substringDiff(k, s1, s2):
    n = len(s1)
    max_len = 0
    
    # Helper function to find max valid length given fixed starting offsets in s1 and s2
    def max_for_offset(i, j):
        nonlocal max_len
        left = 0
        mismatches = 0
        
        # Length of overlapping segment for this diagonal
        length = min(n - i, n - j)
        
        for right in range(length):
            if s1[i + right] != s2[j + right]:
                mismatches += 1
            
            # Shrink window from the left if mismatches exceed k
            while mismatches > k:
                if s1[i + left] != s2[j + left]:
                    mismatches -= 1
                left += 1
            
            current_window = right - left + 1
            if current_window > max_len:
                max_len = current_window

    # Check diagonals starting at (i, 0)
    for i in range(n):
        max_for_offset(i, 0)
        
    # Check diagonals starting at (0, j)
    for j in range(1, n):
        max_for_offset(0, j)

    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        k = int(first_multiple_input[0])

        s1 = first_multiple_input[1]

        s2 = first_multiple_input[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna