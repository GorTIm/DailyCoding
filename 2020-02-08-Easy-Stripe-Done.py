"""
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive 
run of 1s in its binary representation.

For example, given 156, you should return 3.

"""

def longestOnes(n:int) -> int:
    binary_form=intToBinary(n)
    left=-1
    longestL=0
    for i in range(len(binary_form)):
        if int(binary_form[i])==1:
            if left<0:
                left=i
                longestL=max(longestL,1)
            else:
                longestL=max(longestL,i-left+1)
        else:
            left=-1

    return longestL

def intToBinary(n:int) -> str:
    result=""
    while n//2>0:
        result=str(n%2)+result
        n//=2
    result=str(n%2)+result

    return result


if __name__=="__main__":
    integer=input("Please enter an int: ")
    print(longestOnes(int(integer)))