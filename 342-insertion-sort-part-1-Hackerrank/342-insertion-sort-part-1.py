#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Store the last element (the unsorted value)
    target = arr[-1]
    i = n - 2

    # Shift elements to the right until we find the correct spot for target
    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    # Place the target in its correct sorted position
    arr[i + 1] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna