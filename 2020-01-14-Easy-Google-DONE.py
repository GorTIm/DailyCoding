"""This problem was asked by Google.

Given an array of elements, 
return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], 
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

"""

def longest_distinct_subarray(num_list):
    longest_length=0
    pivot=1
    for i in range(len(num_list)):
        while pivot<len(num_list):
            if num_list[pivot] in num_list[i:pivot]:
                break
            else:
                pivot+=1
        if len(num_list[i:pivot])>longest_length:
            longest_length=len(num_list[i:pivot])
        

    return longest_length



if __name__=="__main__":
    #L=[5, 1, 3, 5, 2, 3, 4, 1]
    L=[1,1,2,1,1]
    print(longest_distinct_subarray(L))