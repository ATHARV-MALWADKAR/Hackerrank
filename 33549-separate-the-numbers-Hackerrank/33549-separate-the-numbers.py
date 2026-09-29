#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    
    # The first number cannot have a length greater than half the string length
    for length in range(1, n // 2 + 1):
        first_num = s[:length]
        
        # Disallow leading zeroes
        if first_num.startswith('0'):
            break
            
        first_val = int(first_num)
        built_str = ""
        current_val = first_val
        
        # Generate the sequence by repeatedly adding 1
        while len(built_str) < n:
            built_str += str(current_val)
            current_val += 1
            
        # Check if the generated sequence matches the original string s
        if built_str == s:
            print(f"YES {first_num}")
            return
            
    print("NO")
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna