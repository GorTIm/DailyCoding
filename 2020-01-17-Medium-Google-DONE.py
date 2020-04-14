"""
This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start at the beginning of the array 
and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. 
Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], 
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""

false_set=set()
def toTheEnd(L,start_index):
    if start_index==len(L)-1:
        return True
    elif L[start_index]==0:
        return False
    elif start_index in false_set:
        return False
    else:
        for steps in range(1,L[start_index]+1):
            new_index=start_index+steps
            if toTheEnd(L,new_index):
                return True
            false_set.add(new_index)
        return False


if __name__=="__main__":
    L=[1, 0, 1, 1, 0]
    print(toTheEnd(L,0))
