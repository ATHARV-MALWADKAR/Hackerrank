#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

import sys

MOD = 10**9 + 7
MAX_N = 100005

# Precompute factorials and modular inverse factorials
fact = [1] * MAX_N
inv_fact = [1] * MAX_N

for i in range(1, MAX_N):
    fact[i] = (fact[i - 1] * i) % MOD

inv_fact[MAX_N - 1] = pow(fact[MAX_N - 1], MOD - 2, MOD)
for i in range(MAX_N - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

prefix_counts = []

def initialize(s):
    global prefix_counts
    n = len(s)
    # Prefix count array: prefix_counts[i][c] = count of char c in s[0:i]
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    
    for i, char in enumerate(s):
        for c in range(26):
            prefix_counts[i + 1][c] = prefix_counts[i][c]
        prefix_counts[i + 1][ord(char) - ord('a')] += 1

def answerQuery(l, r):
    # Get character counts in 1-indexed range s[l..r]
    counts = [prefix_counts[r][c] - prefix_counts[l - 1][c] for c in range(26)]
    
    total_pairs = 0
    odd_count = 0
    denom = 1
    
    for cnt in counts:
        pairs = cnt // 2
        total_pairs += pairs
        denom = (denom * inv_fact[pairs]) % MOD
        if cnt % 2 == 1:
            odd_count += 1
            
    # Distinct permutations of pairs: (total_pairs!) / (p1! * p2! * ... * p26!)
    num_permutations = (fact[total_pairs] * denom) % MOD
    
    # If there are odd-frequency characters, any one of them can go in the center
    center_choices = max(1, odd_count)
    
    return (center_choices * num_permutations) % MOD
#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna