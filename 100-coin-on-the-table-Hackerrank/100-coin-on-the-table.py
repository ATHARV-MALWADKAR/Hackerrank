#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'coinOnTheTable' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER k
#  3. STRING_ARRAY board
#

import collections

def coinOnTheTable(m, k, board):
    n = len(board)
    
    # Locate the target '*'
    target_r, target_c = -1, -1
    for r in range(n):
        for c in range(m):
            if board[r][c] == '*':
                target_r, target_c = r, c
                break
        if target_r != -1:
            break

    # Directions: U, D, L, R
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    # min_cost[r][c][steps] = minimum operations to reach (r, c) at time 'steps'
    INF = float('inf')
    min_cost = [[[INF] * (k + 1) for _ in range(m)] for _ in range(n)]
    
    # Priority queue / Deque for 0-1 BFS: (cost, r, c, steps)
    dq = collections.deque([(0, 0, 0, 0)])
    min_cost[0][0][0] = 0

    while dq:
        cost, r, c, steps = dq.popleft()

        if cost > min_cost[r][c][steps]:
            continue

        if steps == k:
            continue

        for move, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                # Cost is 0 if direction matches existing board character, otherwise 1
                add_cost = 0 if board[r][c] == move else 1
                new_cost = cost + add_cost

                if new_cost < min_cost[nr][nc][steps + 1]:
                    min_cost[nr][nc][steps + 1] = new_cost
                    if add_cost == 0:
                        dq.appendleft((new_cost, nr, nc, steps + 1))
                    else:
                        dq.append((new_cost, nr, nc, steps + 1))

    # Find the minimum operations to reach target in <= k steps
    ans = min(min_cost[target_r][target_c])
    return ans if ans != INF else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    board = []

    for _ in range(n):
        board_item = input()
        board.append(board_item)

    result = coinOnTheTable(m, k, board)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna