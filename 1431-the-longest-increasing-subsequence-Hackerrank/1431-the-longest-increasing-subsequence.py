import sys

n = int(input())

class BTreeInterval():
    def __init__(self, n, max):
        self.intervals = [None] * (n + 1)
        self.intervals[0] = (0, max)
        self.current_max = 0
        self.num_max = max
    def get(self, num):
        
        return self.get1(num, self.current_max / 2, 0, self.current_max)
    def get1(self, num, i, fr, to):
        i = int(i)
        #print('intervals:{0} i: {1} from: {2} to: {3}'.format(self.intervals, i, fr, to))
        if fr == to:
            return i
        if num >= self.intervals[i][0] and num < self.intervals[i][1]:
            return i
        if num < self.intervals[i][0]:
            return self.get1(num, (fr + i - 1) / 2, fr, i - 1)
        else:
            return self.get1(num, (i + 1 + to) / 2, i + 1, to)
     
    def set(self, num, i):
        if self.current_max >= i and num >= self.intervals[i][0]:
            return False
        self.intervals[i-1] = (self.intervals[i-1][0], num)
        if i > self.current_max:
            self.current_max = i
            self.intervals[i] = (num, self.num_max)
        else:
            self.intervals[i] = (num, self.intervals[i][1])
        
        return True
        
nums = []

for _ in range(n):
    nums += [int(input())]
    

MAX = 100001

cache = [0] * MAX
local_max = 0

max = 1

btree = BTreeInterval(n, MAX)


for i in range(n):
    
    prev_val = btree.get(nums[i] - 1)
    #print('prev_val: {0} current_num: {1}'.format(prev_val, nums[i]) )
    flag = btree.set(nums[i], prev_val + 1)
    
    if flag and prev_val + 1 > max:
        max = prev_val + 1
#print(btree.intervals[0:(n+1)])            
print(max)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna