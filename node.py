class Node:
    def __init__(self,val=None):
        if val is not None:
            self.val=val
        self.next=None
        
    @staticmethod
    def createLinkedList(L):
        head=Node(L[0])
        temp=head
        #pointer will be created after object instantiated, then point to it
        for i in range(1,len(L)):
            temp.next=Node(L[i])
            temp=temp.next
        
        return head
