# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0 
        #To find the number of nodes in the linked list
        while curr:
            count += 1
            curr = curr.next
        node = head
        #counter to check whether middle node reached or not
        i = 1
        #To see whether the number of nodes are odd or even
        if count % 2 == 0:
            #to find second middle node when even number of nodes
            mid = (count//2)+1    
        else:
            mid = (count+1)//2
        while i < mid:
            i += 1 
            node = node.next   
        return node       


