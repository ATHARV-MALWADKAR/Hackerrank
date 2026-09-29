#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Pair each price with its original year (0-indexed position)
    indexed_prices = [(p, i) for i, p in enumerate(price)]
    
    # Sort prices in ascending order
    indexed_prices.sort()
    
    min_loss = float('inf')
    
    # Compare adjacent elements in the sorted list
    for i in range(1, len(indexed_prices)):
        higher_price, buy_year = indexed_prices[i]
        lower_price, sell_year = indexed_prices[i - 1]
        
        # Valid loss: bought before selling (buy_year < sell_year)
        if buy_year < sell_year:
            loss = higher_price - lower_price
            min_loss = min(min_loss, loss)
            
    return min_loss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna