# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #base case
        if not root:
            return root
        #BFS ---> Level order Traversal
        #Another way of phrasing the same problem is the right most value from each level
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            #the loop runs for each level
            for node in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr.val)
        return res    
