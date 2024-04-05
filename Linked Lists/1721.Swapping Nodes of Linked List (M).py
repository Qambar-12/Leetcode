# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #using two-pointer approach
        #Observation : Distance k would be same from both start and end of list
        curr = head
        #since the list is 1-indexed iterating to k-1
        for i in range(k-1):
            curr = curr.next
        left = curr
        #loop runs until my curr pointer reaches end of linked list
        #so it is guaranteed that at point our right pointer would be at k distance from end
        right = head
        while curr.next:
            curr = curr.next
            right = right.next
        #finally swapping the values of nodes in a single line (no need of tempVar in python)
        left.val , right.val = right.val , left.val    

        return head