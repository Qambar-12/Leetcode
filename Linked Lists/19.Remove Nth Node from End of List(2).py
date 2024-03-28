# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Two pointer solution creating an offset of n+1 in between left and right pointers where +1 is due to dummy node
        #O(n) solution (linear time complexity)
        #as soon as right reaches null our left pointer is one behind our target 
        dummy = ListNode(0,head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        #to delete node chaining with the next node
        left.next = left.next.next
        #because we actually donot want to include dummy node while returning
        return dummy.next        
