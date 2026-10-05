#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def abbreviation(a, b):
    n, m = len(a), len(b)
    
    # dp[i][j] = whether prefix a[:i] can form prefix b[:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Base case for matching 'a' prefix to empty 'b'
    for i in range(1, n + 1):
        if a[i - 1].islower():
            dp[i][0] = dp[i - 1][0]
            
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            char_a = a[i - 1]
            char_b = b[j - 1]
            
            if char_a.isupper():
                if char_a == char_b:
                    dp[i][j] = dp[i - 1][j - 1]
            else:
                if char_a.upper() == char_b:
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
    return "YES" if dp[n][m] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna