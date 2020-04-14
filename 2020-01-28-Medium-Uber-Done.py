"""
This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

def findMinInRotate(L):
    bot=0
    up=len(L)-1
    pivot=0
    while bot<up:
        mid=(bot+up)//2
        if mid==0 or L[mid]<L[mid-1]:
            pivot=mid
            break
        else:
            if L[mid]<L[up]:
                up=mid
            else:
                bot=mid

    return L[pivot]


if __name__=="__main__":
    Li=[5,7,9,10,3,4]
    print(findMinInRotate(Li))