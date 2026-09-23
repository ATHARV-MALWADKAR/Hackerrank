#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Initialize min and max scores with the first game's score
    min_score = scores[0]
    max_score = scores[0]
    
    # Initialize break counters
    min_breaks = 0
    max_breaks = 0
    
    # Iterate through the rest of the games
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_breaks += 1
        elif score < min_score:
            min_score = score
            min_breaks += 1
            
    return [max_breaks, min_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna