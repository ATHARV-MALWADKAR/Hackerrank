import sys
from collections import deque

# Increase recursion depth for deep DFS paths in Hopcroft-Karp
sys.setrecursionlimit(5000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    idx = 3
    bikers = []
    for _ in range(n):
        bikers.append((int(input_data[idx]), int(input_data[idx + 1])))
        idx += 2

    bikes = []
    for _ in range(m):
        bikes.append((int(input_data[idx]), int(input_data[idx + 1])))
        idx += 2

    # Precompute squared Euclidean distances
    dist_sq = []
    unique_dists = set()
    for i in range(n):
        row = []
        bx, by = bikers[i]
        for j in range(m):
            kx, ky = bikes[j]
            d = (bx - kx) ** 2 + (by - ky) ** 2
            row.append(d)
            unique_dists.add(d)
        dist_sq.append(row)

    sorted_dists = sorted(list(unique_dists))

    # Hopcroft-Karp algorithm for Maximum Bipartite Matching
    def max_matching(max_dist):
        pair_u = [-1] * n  # biker -> bike
        pair_v = [-1] * m  # bike -> biker
        dist = [0] * n

        def bfs():
            queue = deque()
            for u in range(n):
                if pair_u[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')

            found_free = False
            while queue:
                u = queue.popleft()
                for v in range(m):
                    if dist_sq[u][v] <= max_dist:
                        matched_u = pair_v[v]
                        if matched_u == -1:
                            found_free = True
                        elif dist[matched_u] == float('inf'):
                            dist[matched_u] = dist[u] + 1
                            queue.append(matched_u)
            return found_free

        def dfs(u):
            for v in range(m):
                if dist_sq[u][v] <= max_dist:
                    matched_u = pair_v[v]
                    if matched_u == -1 or (dist[matched_u] == dist[u] + 1 and dfs(matched_u)):
                        pair_u[u] = v
                        pair_v[v] = u
                        return True
            dist[u] = float('inf')
            return False

        matching = 0
        while bfs():
            for u in range(n):
                if pair_u[u] == -1 and dfs(u):
                    matching += 1
        return matching

    # Binary Search over valid squared distance values
    low, high = 0, len(sorted_dists) - 1
    ans = sorted_dists[-1]

    while low <= high:
        mid = (low + high) // 2
        cand_dist = sorted_dists[mid]

        if max_matching(cand_dist) >= k:
            ans = cand_dist
            high = mid - 1
        else:
            low = mid + 1

    print(ans)

if __name__ == '__main__':
    main()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna