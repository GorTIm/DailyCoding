"""
This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. 
For example, given 48975, the next permutation would be 49578.

"""
def nextPermutation(integer):
    integer=str(integer)
    num_list=[s for s in integer]
    n=len(num_list)
    re=""
    swap=False
    for i in range(-1,-n+1,-1):
        if num_list[i]>num_list[i-1]:
            num_list[i],num_list[i-1]=num_list[i-1],num_list[i]
            swap=True
            break

    if swap:
        temp=num_list[-n:i]
        for ele in temp:
            re+=ele
        temp=num_list[i:]
        temp.sort()
        for ele in temp:
            re+=ele
    else:
        num_list.sort()
        index=num_list.index(integer[0])+1
        re+=num_list[index]
        num_list.pop(index)
        for ele in num_list:
            re+=ele

    return int(re)


if __name__=="__main__":
    i=int(input("Enter an int: "))
    re=nextPermutation(i)
    print(re)


