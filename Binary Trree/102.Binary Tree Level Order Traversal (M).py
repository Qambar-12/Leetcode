# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS Iterative (Queues--->Level Order Traversal)
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        #while queue is not empty means all node values have not been traversed yet
        while q:
            val = []
            #this loop traverses all in the values in a certain level first
            for i in range(len(q)):
                currNode = q.popleft()
                val.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            #after each level appending its values to 2D res array
            res.append(val)
        return res
