#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Helper function to count minimum swaps to match a target sorted array
    def count_swaps(target_arr):
        # Map element value to its current index in a working copy of arr
        pos = {val: i for i, val in enumerate(arr)}
        working_arr = arr.copy()
        swaps = 0

        for i in range(len(working_arr)):
            # If current element is not in its correct position
            if working_arr[i] != target_arr[i]:
                swaps += 1
                
                # Element that should be at index i
                correct_val = target_arr[i]
                current_val = working_arr[i]
                correct_idx = pos[correct_val]

                # Swap elements in working array
                working_arr[i], working_arr[correct_idx] = working_arr[correct_idx], working_arr[i]

                # Update positions in the map
                pos[current_val] = correct_idx
                pos[correct_val] = i

        return swaps

    # Target sorted orders
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)

    # Return the minimum swaps needed between ascending and descending targets
    return min(count_swaps(sorted_asc), count_swaps(sorted_desc))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna