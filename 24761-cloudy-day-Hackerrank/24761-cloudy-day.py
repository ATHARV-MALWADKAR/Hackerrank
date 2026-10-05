#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

from collections import defaultdict

def maximumPeople(p, x, y, r):
    # Events list to process locations along the number line
    events = []
    
    # Cloud events: (location, type, cloud_index)
    # type -1 for cloud start, 1 for cloud end
    for i in range(len(y)):
        start = y[i] - r[i]
        end = y[i] + r[i]
        events.append((start, -1, i))
        events.append((end, 1, i))
        
    # Town events: (location, type, town_index)
    # type 0 so towns are processed after cloud starts and before cloud ends at the same coordinate
    for i in range(len(x)):
        events.append((x[i], 0, i))
        
    # Sort events by position
    events.sort(key=lambda item: (item[0], item[1]))
    
    active_clouds = set()
    already_sunny_people = 0
    cloud_gain = defaultdict(int)
    
    # Sweep line across all events
    for pos, event_type, idx in events:
        if event_type == -1:
            active_clouds.add(idx)
        elif event_type == 1:
            active_clouds.remove(idx)
        else:  # town event
            if len(active_clouds) == 0:
                # Town is not covered by any cloud
                already_sunny_people += p[idx]
            elif len(active_clouds) == 1:
                # Town is covered by exactly one cloud
                single_cloud = next(iter(active_clouds))
                cloud_gain[single_cloud] += p[idx]
                
    # Maximum population freed by removing one cloud
    max_freed = max(cloud_gain.values()) if cloud_gain else 0
    
    return already_sunny_people + max_freed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna