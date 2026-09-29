#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    n = len(arr)
    # The constraints state integers are in range [0, 99]
    buckets = [[] for _ in range(100)]

    for i in range(n):
        idx = int(arr[i][0])
        # Replace the string with '-' for elements in the first half
        s = "-" if i < n // 2 else arr[i][1]
        buckets[idx].append(s)

    # Flatten and print all strings space-separated
    result = []
    for bucket in buckets:
        result.extend(bucket)

    print(" ".join(result))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna