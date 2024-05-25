# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if not head or not head.next:
            return head
        #using a dummy node to return to new list after swapping
        dummy = ListNode(0, head)
        prev , curr =  dummy , head
        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second      #used to create link between the swapped node pairs
            # update ptrs
            prev = curr
            curr = nxtPair
        
        return dummy.next   
