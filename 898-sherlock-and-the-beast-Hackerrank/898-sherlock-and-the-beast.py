#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Try to maximize the count of 5's (which must be a multiple of 3)
    fives = n
    
    # Decrease the count of 5's until the remaining count for 3's is divisible by 5
    while fives % 3 != 0:
        fives -= 5
        
    # If fives becomes negative, it's impossible to form a decent number
    if fives < 0:
        print("-1")
    else:
        threes = n - fives
        print("5" * fives + "3" * threes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna