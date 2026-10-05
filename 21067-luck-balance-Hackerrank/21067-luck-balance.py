N, K = map(int, input().strip().split())
luck = 0
important = []

for _ in range(N):
    L, T = map(int, input().strip().split())
    if T == 0:
        luck += L
    else:
        important.append(L)

# Sort important contests in descending order outside the input loop
important.sort(reverse=True)

for l in important:
    if K > 0:
        luck += l
        K -= 1
    else:
        luck -= l

print(luck)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna