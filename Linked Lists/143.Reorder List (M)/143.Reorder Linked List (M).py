# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        arr = []
        #isolating all nodes so that they point to None and append it to an array arr
        while curr:
            arr.append(curr)
            curr = curr.next
            arr[-1].next = None
        
        #Using two-pointer technique relink the nodes
        #and total number of relinkings are len(arr)-1 so maintain a count for it 
        l,r = 0,len(arr)-1
        count = 0
        while l < r:
            if count == len(arr)-1:
                break
            else:
                arr[l].next = arr[r]
                count += 1
                l += 1
            if count == len(arr)-1:
                break
            else:
                arr[r].next = arr[l]
                count += 1
                r -= 1


        
