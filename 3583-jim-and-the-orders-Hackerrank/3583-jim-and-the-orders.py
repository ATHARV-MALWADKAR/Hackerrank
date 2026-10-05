#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Store tuples of (serve_time, customer_number)
    # customer_number is 1-indexed (i + 1)
    delivery_times = []
    
    for i, (order_time, prep_time) in enumerate(orders):
        serve_time = order_time + prep_time
        delivery_times.append((serve_time, i + 1))
        
    # Sort primarily by serve_time, secondarily by customer_number
    delivery_times.sort()
    
    # Return the list of customer numbers in served order
    return [customer for serve_time, customer in delivery_times]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna