#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter

def reverseShuffleMerge(s):
    # Count frequency of each character in s
    total_count = Counter(s)
    
    # Required count for string A is half of total count
    needed = {char: count // 2 for char, count in total_count.items()}
    
    # Remaining count of characters available as we traverse s backwards
    rem = dict(total_count)
    
    stack = []
    
    # Traverse s in reverse order (since reverse(A) maintains original order of A)
    for char in reversed(s):
        if needed[char] > 0:
            # Maintain lexicographical smallest order using a monotonic stack
            while (stack and 
                   char < stack[-1] and 
                   rem[stack[-1]] > needed[stack[-1]]):
                
                popped = stack.pop()
                needed[popped] += 1
                
            stack.append(char)
            needed[char] -= 1
            
        rem[char] -= 1
        
    return "".join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna