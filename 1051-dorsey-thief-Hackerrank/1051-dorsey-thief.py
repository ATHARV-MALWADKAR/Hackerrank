import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    x = int(data[1])
    
    # Group items by weight: weight -> list of values
    items_by_weight = defaultdict(list)
    idx = 2
    for _ in range(n):
        v = int(data[idx])
        a = int(data[idx + 1])
        idx += 2
        if a <= x:
            items_by_weight[a].append(v)
            
    # For each weight, sort values descending and keep at most (x // weight) items
    pruned_items = []
    for w, values in items_by_weight.items():
        values.sort(reverse=True)
        max_needed = x // w
        for v in values[:max_needed]:
            pruned_items.append((w, v))
            
    # 0/1 Knapsack DP for EXACT weight X
    dp = [-1] * (x + 1)
    dp[0] = 0
    
    for weight, value in pruned_items:
        for j in range(x, weight - 1, -1):
            if dp[j - weight] != -1:
                new_val = dp[j - weight] + value
                if new_val > dp[j]:
                    dp[j] = new_val
                    
    if dp[x] == -1:
        print("Got caught!")
    else:
        print(dp[x])

if __name__ == '__main__':
    solve()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna