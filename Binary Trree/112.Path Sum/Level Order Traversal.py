# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #using level order traversal to our benefit (using queues)
        if not root:
            return False
        from collections import deque
        queueNode = deque([root]) 
        queueSum = deque([root.val])   
        while queueNode:
            currNode = queueNode.popleft()
            currSum = queueSum.popleft()
            #checking if the currNode is a leaf node and it corresponding sum for it equal to target
            if not currNode.left and not currNode.right and currSum == targetSum:
                return True
            if currNode.left:
                queueNode.append(currNode.left)
                queueSum.append(currNode.left.val+currSum)
            if currNode.right:
                queueNode.append(currNode.right)
                queueSum.append(currNode.right.val+currSum)           
        return False    
