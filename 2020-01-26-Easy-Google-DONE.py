"""
This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row 
in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, 
eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. 
The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.

"""
"""def findMaxWeight(triangle_li):
    weight=max_weight=0    
    for triangle in triangle_li:
        weight=maxWeightOfPath(triangle)
        if weight>max_weight:
            max_weight=weight
    
    return max_weight
"""
def maxWeightOfPath(li):
    #Assume a array can form a triangle only if it has at least two elements
    #Besides, assume the triangle is congruent
    k=1
    weight=[]
    up_row=li[0]
    while k<len(li):
        down_row=li[k]
        for i in range(len(up_row)):
            for j in range(i,i+2):
                weight.append(up_row[i]+down_row[j])
        up_row=weight.copy()
        weight.clear()
        k+=1
    return max(up_row)



if __name__=="__main__":
    tri=[[1], [2, 3], [1, 5, 1]]
    print(maxWeightOfPath(tri))

