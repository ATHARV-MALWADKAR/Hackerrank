import sys

# Increase recursion depth for tree segment operations
sys.setrecursionlimit(300000)

MAX_D = 100005

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)
        self.build(1, 1, self.n)

    def build(self, node, start, end):
        if start == end:
            # Base value: completing at time `start` with deadline `start` gives overshoot -start
            self.tree[node] = -start
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def push(self, node):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            # Push to left child
            self.tree[2 * node] += val
            self.lazy[2 * node] += val
            # Push to right child
            self.tree[2 * node + 1] += val
            self.lazy[2 * node + 1] += val
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] += val
            self.lazy[node] += val
            return
        self.push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return -float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        self.push(node)
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    max_d = MAX_D
    
    seg_tree = SegmentTree(max_d)
    max_limit = 0

    idx = 1
    out = []
    for _ in range(t):
        d = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2

        max_limit = max(max_limit, d)

        # Adding duration M to task with deadline D shifts all completion times
        # for deadlines >= D by +M
        seg_tree.update(1, 1, max_d, d, max_d, m)

        # Query max overshoot across all active deadlines [1..max_limit]
        ans = seg_tree.query(1, 1, max_d, 1, max_limit)
        
        # Max overshoot cannot be less than 0
        out.append(str(max(0, ans)))

    print('\n'.join(out))

if __name__ == '__main__':
    solve()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna