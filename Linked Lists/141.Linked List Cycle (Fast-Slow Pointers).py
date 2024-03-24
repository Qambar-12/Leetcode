# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Slow-Fast Pointer approach
        slow , fast = head, head
        #returning False outside loop means tail points to null
        #since fast reaches tail faster, if there exists a cycle slow and fast pointers would coincide 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False        
