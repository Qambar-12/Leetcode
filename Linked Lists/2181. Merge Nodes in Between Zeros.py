# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #IN PLACE SOLUTION
        curr = head 
        while curr.next:
            node = curr = curr.next
            while curr.next.val != 0:
                node.val += curr.next.val
                curr = curr.next
            
            curr = curr.next
            node.next = curr.next
        return head.next        