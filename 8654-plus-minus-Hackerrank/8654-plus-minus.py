#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)
    
    print(f"{positive_count / n:.6f}")
    print(f"{negative_count / n:.6f}")
    print(f"{zero_count / n:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna