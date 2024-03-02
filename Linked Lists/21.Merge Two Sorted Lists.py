# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating a dummy node to avoid edge test case of inserting in empty linked list
        dummy = node = ListNode()
        #while both linked lists pointers donot point to null i.e (None)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        #if the linked lists have unqual number of nodes
        node.next = list1 or list2

        #returning the head of the final merged sorted linked list using variable dummy instead of node
        return dummy.next            
