#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#
from collections import Counter

def beautifulPairs(A, B):
    count_A = Counter(A)
    count_B = Counter(B)
    
    # Calculate initial matching elements between A and B
    matches = 0
    for num in count_A:
        if num in count_B:
            matches += min(count_A[num], count_B[num])
            
    # Since we MUST change exactly 1 element in B:
    # If all elements were matched, changing 1 element loses 1 pair.
    # Otherwise, changing 1 unmatched element can form 1 new pair.
    if matches == len(A):
        return matches - 1
    else:
        return matches + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna