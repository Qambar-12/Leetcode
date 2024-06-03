# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = 0
        while curr and curr.next :
            if i == a-1:
                refNode = curr.next
                j = i + 1
                curr.next = list2
            curr = curr.next
            i += 1
        tail2 = curr 
        if a != b:
            while refNode and refNode.next:
                if j == b-1:
                    tail2.next = refNode.next.next
                    refNode.next = None
                refNode = refNode.next
                j += 1       
        else:
            tail2.next = refNode.next

        return list1    
