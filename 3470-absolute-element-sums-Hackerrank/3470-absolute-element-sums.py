import os
import sys
import bisect

def playingWithNumbers(arr, queries):
    n = len(arr)
    arr.sort()
    
    # Prefix sums array for fast range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
        
    current_shift = 0
    results = []
    
    for q in queries:
        current_shift += q
        
        # Binary search for the split point where arr[i] + current_shift < 0
        target = -current_shift
        idx = bisect.bisect_left(arr, target)
        
        # Elements in arr[0...idx-1] are negative after adding current_shift
        neg_sum = -(prefix[idx] + idx * current_shift)
        
        # Elements in arr[idx...n-1] are non-negative after adding current_shift
        pos_sum = (prefix[n] - prefix[idx]) + (n - idx) * current_shift
        
        results.append(neg_sum + pos_sum)
        
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    queries_count = int(input().strip())

    # Read space-separated queries from a single line
    queries = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna