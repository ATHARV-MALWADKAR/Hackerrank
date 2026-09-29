#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    res = []
    k = k % 26  # Normalize shift key
    
    for char in s:
        if 'a' <= char <= 'z':
            # Shift lowercase letter with wrap-around
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            res.append(new_char)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letter with wrap-around
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            res.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            res.append(char)
            
    return "".join(res)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna