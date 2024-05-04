# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    def __str__(self):
        return str(self.val)     


def zigzagLevelOrder(root):
    #base case
    if not root:
        return []
    #BFS --->Level Order Traversal (using deque beacause popping from infront of it is O(1) operation)
    #stausLevel = 0 corresponds to left --> right and vice versa
    statusLevel = 0
    #2D list where each sublist corresponds to a level
    res = []
    from collections import deque
    q = deque([root])
    while q:
        level = []
        for n in range(len(q)):
            currNode = q.popleft()
            level.append(currNode.val)
            #i.e traverse from right to left for the next level by appending right child first
            if not statusLevel:
                if currNode.right:
                    q.append(currNode.right)
                if currNode.left:
                    q.append(currNode.left)
            #i.e traverse from left to right for the next level by appending left child first 
            else:
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)   
        if statusLevel: 
            statusLevel = 0
        else:
            statusLevel = 1                      
        res.append(level)
    return res
print(zigzagLevelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))))) #[[3],[20,9],[15,7]]
