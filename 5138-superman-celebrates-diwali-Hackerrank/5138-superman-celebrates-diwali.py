import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    H = int(input_data[1])
    I = int(input_data[2])
    
    idx = 3
    # count[b][h] storing number of people at floor h of building b
    count = [[0] * (H + 1) for _ in range(N)]
    
    for b in range(N):
        k = int(input_data[idx])
        idx += 1
        for _ in range(k):
            floor = int(input_data[idx])
            count[b][floor] += 1
            idx += 1

    dp = [[0] * (H + 1) for _ in range(N)]
    max_dp = [0] * (H + 1)

    for h in range(1, H + 1):
        for b in range(N):
            # Option 1: Stay in the same building and move down from floor h - 1
            best_prev = dp[b][h - 1]
            
            # Option 2: Jump from another building from floor h - I
            if h >= I:
                best_prev = max(best_prev, max_dp[h - I])
                
            dp[b][h] = count[b][h] + best_prev
            max_dp[h] = max(max_dp[h], dp[b][h])

    print(max_dp[H])

if __name__ == '__main__':
    solve()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna