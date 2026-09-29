#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import Counter

def anagram(s):
    n = len(s)
    
    # If length is odd, it's impossible to divide into two equal substrings
    if n % 2 != 0:
        return -1
        
    mid = n // 2
    s1_counts = Counter(s[:mid])
    s2_counts = Counter(s[mid:])
    
    # Count characters in s1 that are missing or deficient in s2
    changes = 0
    for char, count in s1_counts.items():
        if count > s2_counts[char]:
            changes += count - s2_counts[char]
            
    return changes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna