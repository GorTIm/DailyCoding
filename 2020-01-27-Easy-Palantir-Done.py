"""
This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. 
For example, 1221 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.

"""

def intPalindrome(integer):
    times=0
    temp=integer
    while (temp//10)>=1:
        times+=1
        temp//=10
    while integer>=10:
        if (integer%10)!=(integer//(10**times)):
            return False
        integer-=(integer//(10**times))*(10**times)
        integer//=10
        #key
        times-=2

    return True


if __name__=="__main__":
    while True:
        p=input("Enter integer: ")
        print(intPalindrome(int(p)))


