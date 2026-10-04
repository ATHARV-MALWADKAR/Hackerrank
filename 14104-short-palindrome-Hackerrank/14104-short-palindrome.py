#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    MOD = 10**9 + 7
    
    # c1[x]: Frequency of character x seen so far
    c1 = [0] * 26
    
    # c2[x][y]: Frequency of pair (x, y) seen so far
    c2 = [[0] * 26 for _ in range(26)]
    
    # c3[x]: Count of triples (x, y, y) seen so far for a fixed x
    c3 = [0] * 26
    
    ans = 0
    
    for char in s:
        idx = ord(char) - ord('a')
        
        # Step 4: char serves as the 4th character 'd' (s[d] == s[a] == idx)
        # Add the count of valid triples (idx, y, y) formed so far
        ans = (ans + c3[idx]) % MOD
        
        # Step 3: char serves as the 3rd character 'c' (s[c] == s[b] == idx)
        # Update triples (x, idx, idx) using pairs (x, idx) seen so far
        for x in range(26):
            c3[x] = (c3[x] + c2[x][idx]) % MOD
            
        # Step 2: char serves as the 2nd character 'b' (idx)
        # Update pairs (x, idx) using individual character counts seen so far
        for x in range(26):
            c2[x][idx] = (c2[x][idx] + c1[x]) % MOD
            
        # Step 1: char serves as the 1st character 'a'
        c1[idx] += 1
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna