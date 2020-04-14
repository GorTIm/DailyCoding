"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

"""

def startIndicesOfPattern(s,pattern):
    length=len(pattern)
    result=[]
    for i in range(len(s)-length+1):
        if s[i:i+length]==pattern:
            result.append(i)

    return result

if __name__=="__main__":
    s=input("Enter the string: ")
    pattern=input("Enter the pattern: ")
    print(startIndicesOfPattern(s,pattern))

