#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        
        merged = []
        inversions = left_inv + right_inv
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                # If left[i] > right[j], then right[j] is smaller than all remaining elements in left
                merged.append(right[j])
                inversions += len(left) - i
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inversions

    _, total_shifts = merge_sort(arr)
    return total_shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna