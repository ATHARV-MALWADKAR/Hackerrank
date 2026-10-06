#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arraySplitting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def arraySplitting(arr):
    # Special case: if total sum is 0, we can perform len(arr) - 1 splits
    if sum(arr) == 0:
        return len(arr) - 1
        
    total = sum(arr)
    
    def solve(left, right, total_sum):
        if left >= right or total_sum % 2 != 0:
            return 0
            
        half_sum = total_sum // 2
        curr_sum = 0
        split_idx = -1
        
        for i in range(left, right):
            curr_sum += arr[i]
            if curr_sum == half_sum:
                split_idx = i
                break
            elif curr_sum > half_sum:
                break
                
        if split_idx == -1:
            return 0
            
        left_score = solve(left, split_idx, half_sum)
        right_score = solve(split_idx + 1, right, half_sum)
        
        return 1 + max(left_score, right_score)

    return solve(0, len(arr) - 1, total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna