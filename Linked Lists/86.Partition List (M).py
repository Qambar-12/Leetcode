# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #base case
        if not head :
            return head
        #Dummy Nodes    
        left , right = ListNode() , ListNode()   
        ltail , rtail = left, right
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        #connecting the both partitioned lists
        ltail.next = right.next
        #terminating both lists by pointing rtail to None
        rtail.next = None
        return left.next
