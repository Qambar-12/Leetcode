# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS solution using Queue (where max depth is equal to number of levels in a tree)
        #Level-wise traversal
        if not root :
            return 0
        #using deque --> Double ended queue b/c popping from infront of a list is O(n) operation b.c all indices need to be shifted
        from collections import deque
        queue = deque([root])
        levelCount = 0  
        #when the loop terminates all nodes adding to queue once and popped from front once i.e time complexity is O(n)
        while queue:
            #taking snapshot of each level
            for i in range(len(queue)):
                #currNode points to most recently visited node
                currNode = queue.popleft()
                #Before adding to back of queue checking whether the left and right exist respectively i.e not None
                #here adding left first unlike in dfs b/c queues works on principle of FIFO or LILO unlike stacks
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            #after traversing each level incrementing the levelCount
            levelCount += 1        
        return levelCount                
