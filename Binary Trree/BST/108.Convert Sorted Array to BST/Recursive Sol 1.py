# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #BST ---> A Binary Tree where left node is less than parent and right node is greater than parent
        #Recursive Solution (via helper function)
        def helper(l,r):
            #Base case i.e if left pointer somehow becomes greater than right pointer i.e we have formed the left or right subtree respectively
            if l > r:
                return None
            #mid value is the root node in the sorted array
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            #Recursive calls for left and right subtrees respectively
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)
            #finally we just need to return root
            return root
        
        return helper(0,len(nums)-1)