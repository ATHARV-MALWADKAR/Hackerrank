#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squareSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def squareSubsequences(s):
    MOD = 10**9 + 7
    n = len(s)
    ans = 0

    # Fix the last character of the FIRST half W at index i
    for i in range(n - 1):
        # s1 is left part s[0...i-1], s2 is right part s[i+1...n-1]
        # s[i] must match the last character of the second half
        c = s[i]
        
        # We compute common subsequences between s[0...i-1] and s[i+1...n-1]
        len1 = i
        len2 = n - (i + 1)
        
        if len1 == 0 or len2 == 0:
            # If left side is empty, the first half W consists only of s[i].
            # Count occurrences of s[i] in the right part.
            for k in range(i + 1, n):
                if s[k] == c:
                    ans = (ans + 1) % MOD
            continue

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Base case: 1 for empty matching subsequence
        for j in range(len1 + 1):
            dp[j][0] = 1
        for k in range(len2 + 1):
            dp[0][k] = 1

        for j in range(1, len1 + 1):
            for k in range(1, len2 + 1):
                if s[j - 1] == s[i + 1 + k - 1]:
                    dp[j][k] = (dp[j - 1][k] + dp[j][k - 1]) % MOD
                else:
                    dp[j][k] = (dp[j - 1][k] + dp[j][k - 1] - dp[j - 1][k - 1] + MOD) % MOD

        # For every index k in the right part where s[k] == s[i],
        # add the number of valid common subsequences formed before it
        for k in range(i + 1, n):
            if s[k] == c:
                k_idx = k - (i + 1)  # 1-based index in s2
                ans = (ans + dp[len1][k_idx]) % MOD

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = squareSubsequences(s)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna