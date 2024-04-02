# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BFS Iterative (Queues)
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            from collections import deque
            qP = deque([p])
            qQ = deque([q])
            while qP and qQ:
                #popping from infront of queue and using double ended queue b/c popping from list itself is O(n) operation
                currNodeP = qP.popleft()
                currNodeQ = qQ.popleft()
                if currNodeP.val == currNodeQ.val:
                    if currNodeP.left and currNodeQ.left:
                        qP.append(currNodeP.left)
                        qQ.append(currNodeQ.left)
                    elif not currNodeP.left and not currNodeQ.left:
                        pass
                    else:
                        return False    
                    if currNodeP.right and currNodeQ.right:
                        qP.append(currNodeP.right)
                        qQ.append(currNodeQ.right)
                    elif not currNodeP.right and not currNodeQ.right:
                        pass
                    else:
                        return False    
                else:
                    return False    
            return True    
