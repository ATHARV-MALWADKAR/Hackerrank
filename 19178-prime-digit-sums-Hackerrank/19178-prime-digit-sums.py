import sys

# Set of primes up to max possible 5-digit sum (45)
PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    q = int(input_data[0])
    queries = [int(x) for x in input_data[1:q+1]]
    
    max_n = max(queries)
    MOD = 10**9 + 7

    # Find all valid 5-digit sequences satisfying prime conditions
    valid_5 = []
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                if (d1 + d2 + d3) not in PRIMES:
                    continue
                for d4 in range(10):
                    if (d2 + d3 + d4) not in PRIMES or (d1 + d2 + d3 + d4) not in PRIMES:
                        continue
                    for d5 in range(10):
                        if (
                            (d3 + d4 + d5) in PRIMES and
                            (d2 + d3 + d4 + d5) in PRIMES and
                            (d1 + d2 + d3 + d4 + d5) in PRIMES
                        ):
                            valid_5.append((d1 * 10000 + d2 * 1000 + d3 * 100 + d4 * 10 + d5, d1, d2, d3, d4, d5))

    num_states = len(valid_5)
    state_to_idx = {st[0]: i for i, st in enumerate(valid_5)}

    # Build adjacency transitions
    adj = [[] for _ in range(num_states)]
    for i, (st, d1, d2, d3, d4, d5) in enumerate(valid_5):
        for d6 in range(10):
            if (
                (d4 + d5 + d6) in PRIMES and
                (d3 + d4 + d5 + d6) in PRIMES and
                (d2 + d3 + d4 + d5 + d6) in PRIMES
            ):
                next_st = d2 * 10000 + d3 * 1000 + d4 * 100 + d5 * 10 + d6
                if next_st in state_to_idx:
                    adj[i].append(state_to_idx[next_st])

    # Precompute DP table up to max_n
    ans = [0] * (max(max_n + 1, 6))
    ans[1] = 9
    ans[2] = 90
    ans[3] = sum(1 for d1 in range(1, 10) for d2 in range(10) for d3 in range(10) if (d1 + d2 + d3) in PRIMES)
    ans[4] = sum(
        1 for d1 in range(1, 10) for d2 in range(10) for d3 in range(10) for d4 in range(10)
        if (d1 + d2 + d3) in PRIMES and (d2 + d3 + d4) in PRIMES and (d1 + d2 + d3 + d4) in PRIMES
    )

    curr_dp = [1 if st[1] > 0 else 0 for st in valid_5]
    ans[5] = sum(curr_dp) % MOD

    for n in range(6, max_n + 1):
        next_dp = [0] * num_states
        for u in range(num_states):
            count = curr_dp[u]
            if count:
                for v in adj[u]:
                    next_dp[v] = (next_dp[v] + count) % MOD
        curr_dp = next_dp
        ans[n] = sum(curr_dp) % MOD

    # Output answer for each query
    for n in queries:
        print(ans[n])

if __name__ == '__main__':
    solve()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna