# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #using fast and slow pointers to find middle of linked list
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        #reversing the second half of the linked list
        slow.next = None
        prev = None
        while second :
            tempVar = second.next
            second.next = prev 
            prev = second
            second = tempVar
        #then using two pointer approach to add corresponding value pairs 
        first , second = head , prev
        res = float('-inf')
        while first and second:
            twinSum = first.val + second.val
            res = max(res,twinSum)
            first , second = first.next , second.next
        return res    
