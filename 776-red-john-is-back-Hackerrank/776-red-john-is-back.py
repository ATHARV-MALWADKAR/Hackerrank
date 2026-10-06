#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'redJohn' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def redJohn(n):
    # Step 1: DP for wall tiling (4xn using 4x1 and 1x4 bricks)
    dp = [1] * (n + 1)
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 4]
        
    M = dp[n]
    if M < 2:
        return 0
        
    # Step 2: Sieve of Eratosthenes to count primes <= M
    is_prime = [True] * (M + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= M:
        if is_prime[p]:
            for i in range(p * p, M + 1, p):
                is_prime[i] = False
        p += 1
        
    return sum(is_prime)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna