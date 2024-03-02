# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #Handle the case where list is empty
        if head is None:
            return None
        
        #removing leading nodes with value val
        while head and head.val == val:
            head = head.next    
    
        currNode = head
        #currNode.next included in while loop condition to avoid attribute error i.e its value is not None
        while currNode and currNode.next:
            if currNode.next.val == val:
                currNode.next = currNode.next.next
                #to accomodate consecutive values val occurence in linked list
                while currNode and currNode.next and currNode.next.val == val :
                    currNode.next = currNode.next.next
            #updating the current node pointer
            currNode = currNode.next
        
        return head                
