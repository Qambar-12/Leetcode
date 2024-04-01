# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Two pass solution 
        curr = head
        count = 0
        while curr :
            curr = curr.next
            count += 1
        curr = head
        c = 0
        targetCount = count - n  
        if  targetCount :
            while curr:
                print("hello")
                if c == targetCount-1 :
                    curr.next = curr.next.next      
                curr = curr.next
                c += 1
        else:
            head = head.next    
        return head
