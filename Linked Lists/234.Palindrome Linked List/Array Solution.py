# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Time and space complexity both are O(n) where n is the size of linked list
        arr = []
        currNode = head
        while currNode:
            arr.append(currNode.val)
            currNode = currNode.next

        #or using two pointers approach
        #i,j = 0,len(arr)-1
        #while i<=j:
            #if arr[i] != arr[j]:
                #return False
            #i += 1
            #j -= 1
        #return True    
            
        return arr == arr[::-1]    
