#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Frequency array for counting sort (max value of expenditure is 200)
    count = [0] * 201
    
    # Initialize the frequency map with the first 'd' elements
    for i in range(d):
        count[expenditure[i]] += 1
        
    notifications = 0

    # Helper function to return 2 * median from the frequency array
    def get_double_median():
        if d % 2 == 1:
            target = d // 2 + 1
            current_sum = 0
            for val in range(201):
                current_sum += count[val]
                if current_sum >= target:
                    return 2 * val
        else:
            first_target = d // 2
            second_target = d // 2 + 1
            first_val = None
            second_val = None
            current_sum = 0
            for val in range(201):
                current_sum += count[val]
                if first_val is None and current_sum >= first_target:
                    first_val = val
                if current_sum >= second_target:
                    second_val = val
                    return first_val + second_val
        return 0

    # Iterate through expenditures starting from day d
    for i in range(d, len(expenditure)):
        current_exp = expenditure[i]
        
        # Check if notification condition is met
        if current_exp >= get_double_median():
            notifications += 1
            
        # Slide the window: add current day, remove oldest day
        count[current_exp] += 1
        count[expenditure[i - d]] -= 1

    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna