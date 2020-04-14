"""
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed 
using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
"""



def interleave_stack(S):
    queue=[]
    orderedNumber=1
    while orderedNumber<len(S):
        for i in range(len(S)-orderedNumber):
            itemFromS=S.pop()
            queue.append(itemFromS)      
        for i in range(len(queue)-1):
            itemFromQ=queue.pop(0)
            S.append(itemFromQ)
        orderedNumber+=1
    lastItem=queue.pop()
    S.append(lastItem)
    
    return S
    
if __name__=="__main__":
    stack=[1, 2, 3, 4]
    print(interleave_stack(stack))