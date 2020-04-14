"""
This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove 
to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed 
and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

#greedy

def min_intervals(L):
    L.sort()
    interval_map={}
    numToRemove=0
    for i in range(len(L)):
        if not (overlap(L[i],interval_map)):
            interval_map[L[i][0]]=L[i][1]
        else:
            numToRemove+=1

    return numToRemove

def overlap(interval,inter_map):
    for key in inter_map:
        if not (interval[0]>=inter_map[key] or interval[1]<=key):
            return True
    
    return False

if __name__=="__main__":
    Li=[(7, 9), (2, 4), (1, 10)]
    print(min_intervals(Li))

