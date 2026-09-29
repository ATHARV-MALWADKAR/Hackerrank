def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        # Bug fix: Changed (j > 0) to (j >= 0) to allow checking index 0
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str, ar)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna