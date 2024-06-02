# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #approach 2 : reverse the list first and then traverse by maintaining curr_max
        #helper function
        def reverse(head):
            prev , curr = None , head
            while curr:
                temp = curr.next
                curr.next = prev
                prev , curr = curr , temp
            return prev
        #first reversal of linked list so that we can maintain a curr_max
        head = reverse(head)
        curr = head
        curr_max = curr.val 
        while curr.next:
            #remove the node
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                #update curr_max and move pointer forward
                curr_max = curr.next.val
                curr = curr.next    
        #again reverse before returning to preserve the original direction of pointers
        return reverse(head)        
