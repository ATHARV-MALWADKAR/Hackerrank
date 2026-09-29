import sys
from collections import deque
from bisect import bisect_left, bisect_right

class TrieNode:
    __slots__ = ('children', 'fail', 'indices', 'prefix_health', 'dict_link')
    def __init__(self):
        self.children = {}
        self.fail = None
        self.dict_link = None
        self.indices = []
        self.prefix_health = [0]

def build_aho_corasick(genes, health):
    root = TrieNode()
    
    # 1. Build Trie with prefix health totals
    for idx, (gene, h) in enumerate(zip(genes, health)):
        curr = root
        for char in gene:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.indices.append(idx)
        curr.prefix_health.append(curr.prefix_health[-1] + h)
        
    # 2. Build Failure and Dictionary Output Links via BFS
    queue = deque()
    for child in root.children.values():
        child.fail = root
        queue.append(child)
        
    while queue:
        curr = queue.popleft()
        
        # Shortcut to bypass non-gene nodes on failure paths
        if curr.fail and curr.fail.indices:
            curr.dict_link = curr.fail
        elif curr.fail:
            curr.dict_link = curr.fail.dict_link

        for char, child in curr.children.items():
            fail_node = curr.fail
            while fail_node and char not in fail_node.children:
                fail_node = fail_node.fail
            child.fail = fail_node.children[char] if fail_node else root
            queue.append(child)
            
    return root

def get_health_in_range(node, first, last):
    if not node.indices:
        return 0
    left = bisect_left(node.indices, first)
    right = bisect_right(node.indices, last)
    return node.prefix_health[right] - node.prefix_health[left]

def calculate_strand_health(root, first, last, d):
    total_health = 0
    curr = root
    
    for char in d:
        while curr and char not in curr.children:
            curr = curr.fail
        curr = curr.children[char] if curr else root
        
        # Follow dictionary links directly to nodes with gene matches
        temp = curr
        while temp and temp != root:
            if temp.indices:
                total_health += get_health_in_range(temp, first, last)
            temp = temp.dict_link
            
    return total_health

def main():
    input_line = sys.stdin.readline
    
    n_str = input_line()
    if not n_str:
        return
    n = int(n_str.strip())
    
    genes = input_line().split()
    health = [int(x) for x in input_line().split()]
    
    s = int(input_line().strip())
    
    root = build_aho_corasick(genes, health)
    
    min_health = float('inf')
    max_health = 0
    
    for _ in range(s):
        parts = input_line().split()
        if not parts:
            continue
        first = int(parts[0])
        last = int(parts[1])
        d = parts[2]
        
        strand_health = calculate_strand_health(root, first, last, d)
        min_health = min(min_health, strand_health)
        max_health = max(max_health, strand_health)
        
    print(f"{min_health} {max_health}")

if __name__ == '__main__':
    main()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna