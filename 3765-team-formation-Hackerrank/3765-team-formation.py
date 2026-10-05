import sys
from collections import defaultdict
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        if n == 0:
            print(0)
            continue
            
        skills = []
        for _ in range(n):
            skills.append(int(input_data[idx]))
            idx += 1
            
        # Sort skills to process contestants in ascending order
        skills.sort()
        
        # Maps skill level -> min-heap of team sizes ending at that skill level
        teams = defaultdict(list)
        
        for x in skills:
            # If there is a team ending at x - 1, attach x to the smallest team ending at x - 1
            if teams[x - 1]:
                smallest_team_len = heapq.heappop(teams[x - 1])
                heapq.heappush(teams[x], smallest_team_len + 1)
            else:
                # Start a new team of size 1 ending at x
                heapq.heappush(teams[x], 1)
                
        # Find the minimum team size across all formed teams
        min_size = float('inf')
        for heap in teams.values():
            if heap:
                min_size = min(min_size, heap[0])
                
        print(min_size)

if __name__ == '__main__':
    solve()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna