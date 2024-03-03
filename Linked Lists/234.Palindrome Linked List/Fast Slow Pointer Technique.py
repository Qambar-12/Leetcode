# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #intializing both pointers fast and slow to head
        fast , slow = head , head
        #after loop breaks slow would point to middle (node) of linked list
        #Because in each iteration fast pointer updates by skipping a node in between while slow pointer continues to traverse linked list in linear fashion
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        #reversing the second half of the list so that it can be compared with first half to check for palindrome
        prev = None
        #after loop breaks i.e slow.next points to None, variable prev holds the head of reversed linked list
        while slow:
            tempVar = slow.next
            slow.next = prev
            prev = slow
            slow = tempVar

        #finally now middle node's next points to None
        #using two pointer technique like in array solution to check for palindrome
        i , j = head,prev
        while j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True            
