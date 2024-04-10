# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currL1 , currL2 = l1 , l2
        carry = 0
        #creating a dummy node
        res = head = ListNode()
        while currL1 or currL2:
            if currL1 : 
                val1 = currL1.val 
                currL1 = currL1.next
            else:
                val1 = 0           
            if currL2 : 
                val2 = currL2.val 
                currL2 = currL2.next
            else:
                val2 = 0    
            Sum = val1 + val2 + carry
            if Sum < 10:
                res.next = ListNode(Sum)
            else:
                print(Sum)
                res.next = ListNode(Sum%10) 
            res = res.next       
            carry = Sum // 10 
        #after loop terminates checking if there is any extra carry left to accomodate
        if Sum >= 10:
            res.next = ListNode(carry)
        
        return head.next