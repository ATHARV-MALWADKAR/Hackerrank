#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'specialSubCubes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY cube as parameter.
#

import math

def specialSubCubes(cube):
    # Calculate n from n^3 length of the flattened cube array
    n = round(len(cube) ** (1/3))
    
    # Map flattened 0-indexed array to 1-indexed 3D grid V[x][y][z]
    V = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    idx = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                V[x][y][z] = cube[idx]
                idx += 1
                
    ans = [0] * (n + 1)
    
    # DP table storing maximum value in sub-cubes of size L x L x L at top-left-front (x, y, z)
    current_dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 2)]
    
    # Base case: Size L = 1
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                val = V[x][y][z]
                current_dp[x][y][z] = val
                if val == 1:
                    ans[1] += 1
                    
    # Transitions for L from 2 to n
    for L in range(2, n + 1):
        next_dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 2)]
        for x in range(1, n - L + 2):
            for y in range(1, n - L + 2):
                for z in range(1, n - L + 2):
                    mx = max(
                        current_dp[x][y][z],
                        current_dp[x + 1][y][z],
                        current_dp[x][y + 1][z],
                        current_dp[x][y][z + 1],
                        current_dp[x + 1][y + 1][z],
                        current_dp[x + 1][y][z + 1],
                        current_dp[x][y + 1][z + 1],
                        current_dp[x + 1][y + 1][z + 1]
                    )
                    next_dp[x][y][z] = mx
                    if mx == L:
                        ans[L] += 1
        current_dp = next_dp
        
    return ans[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        cube = list(map(int, input().rstrip().split()))

        result = specialSubCubes(cube)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna