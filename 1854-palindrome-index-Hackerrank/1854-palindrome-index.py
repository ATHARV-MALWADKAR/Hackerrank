#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        if s[l] != s[r]:
            # Test if skipping s[l] makes the remaining substring a palindrome
            sub = s[l+1 : r+1]
            if sub == sub[::-1]:
                return l
            # Otherwise, removing s[r] must form a palindrome
            return r
        l += 1
        r -= 1
        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna