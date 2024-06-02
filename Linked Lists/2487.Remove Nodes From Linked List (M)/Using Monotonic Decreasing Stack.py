# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #approach 1 : we have to make monotonic decreasing linked list or more simply stack
        curr = head
        stack = []
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)    
            curr = curr.next
        #use of a dummy node
        dummy = ListNode()  
        curr = dummy  
        for node in stack:
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next         