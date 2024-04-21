# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #since width cannot be less than 1
        maxWidth =  1
        #Level order Traversal  ---> BFS
        from collections import deque
        q = deque([[root,1]])
        while q:
            #the difference between rightmost and leftmost nodeIDs respectively
            diff = q[-1][1] - q[0][1] + 1
            maxWidth = max(maxWidth,diff)
            #iterate over all node in current level
            for n in range(len(q)):
                #nodeID numbering for all non-null and null nodes which intially starts from 1 for root node
                #if a node is numbered i its left child would be numbered '2*i' and right child '2i*+1'
                node,nodeID = q.popleft()    
                if node.left:
                    q.append([node.left,nodeID*2])   
                if node.right:
                    q.append([node.right,(nodeID*2)+1])                       
        return maxWidth            

