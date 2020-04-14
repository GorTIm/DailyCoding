"""
This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. 
The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

"""

"""
Assume that 
class tree_node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right==None

"""


sums={}
def mostFrequentSum(Root):
    subtreeSums(Root)
    frequency_of_sum=0
    for i in sums:
        if sums[i]>most_frequent_sum:
            most_frequent_sum=sums[i]

    return most_frequent_sum

    
def subtreeSums(root_node):
    subtree_sum=0
    if root_node.left==None and root_node.right==None:
        subtree_sum=root_node.val
    else:
        left_sum=self.subtree(root_node.left)
        right_sum=elf.subtree(root_node.right)
        subtree_sum=left_sum+right_sum+root_node.val

    if  subtree_sum in sums:
        sums[subtree_sum]+=1
    else:
        sums[subtree_sum]=1
    
    return subtree_sum
