"""
This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
"""

"""
def __init__(self,val=None):
    if val is not None:
        self.val=val
    self.next=None
"""
from node import Node

#Method 1, recursively copy
def reverseGraph(head:Node) -> Node:
    if head.next==None:
        return Node(head.val)
    reversed_graph=reverseGraph(head.next)
    temp=reversed_graph
    while temp.next is not None:
        temp=temp.next
    temp.next=Node(head.val)


    return reversed_graph

h=Node.createLinkedList(["a","b","c","d"])
re=reverseGraph(h)
while re is not None:
    print(re.val+"->")
    re=re.next

