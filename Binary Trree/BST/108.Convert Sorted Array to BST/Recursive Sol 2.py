# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #BST ---> A Binary Tree where left node is less than parent and right node is greater than parent
        #Recursive Solution
        #Base case
        if len(nums) == 0:
            return None
        mid = (len(nums)-1)//2
        root = TreeNode(nums[mid])
        #recursive calls for left and right subtrees respectively
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        #finally just need to return the root node
        return root
        