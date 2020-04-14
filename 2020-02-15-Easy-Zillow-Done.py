"""
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, 、
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, 
and so on. Create an algorithm to find the nth sevenish number.

"""


def findNSevenish(n):
    #given that n start from 1
    n=int(n)-1
    i=0
    result=[1]
    pow_seven=1
    while i<=n:
        pow_seven*=7
        result.append(pow_seven)
        i+=1
        temp=[]
        for j in range(len(result)-1):
            temp.append(result[j]+result[-1])
            i+=1
        result.extend(temp)
    
    return result[n]

if __name__=="__main__":
    n=input("Enter an int:")
    print(findNSevenish(n))