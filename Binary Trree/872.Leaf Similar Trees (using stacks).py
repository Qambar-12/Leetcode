# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 , seq2 = [],[]
        stack1 , stack2 = [root1],[root2]
        while stack1 or stack2:
            if stack1:
                node1 = stack1.pop()
                if node1:
                    if not node1.left and not node1.right:
                        seq1.append(node1.val)
                    else:
                        if node1.left:
                            stack1.append(node1.left)  
                        if node1.right:
                            stack1.append(node1.right)
            if stack2:
                node2 = stack2.pop()
                if node2:
                    if not node2.left and not node2.right:
                        seq2.append(node2.val)
                    else:
                        if node2.left:
                            stack2.append(node2.left)  
                        if node2.right:
                            stack2.append(node2.right)
        
        return seq1 == seq2                
