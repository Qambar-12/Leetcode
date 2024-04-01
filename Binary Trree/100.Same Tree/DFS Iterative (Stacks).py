# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS Iterative
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        else:
            stackP = [p]
            stackQ = [q]
            while stackP and stackQ:
                currNodeP = stackP.pop()
                currNodeQ = stackQ.pop()    
                if currNodeP.val == currNodeQ.val:
                    if currNodeP.right and currNodeQ.right:
                        stackP.append(currNodeP.right)
                        stackQ.append(currNodeQ.right)
                    elif not currNodeP.right and not currNodeQ.right:
                        pass
                    else:
                        return False       
                    if currNodeP.left and currNodeQ.left:
                        stackP.append(currNodeP.left)
                        stackQ.append(currNodeQ.left)
                    elif not currNodeP.left and not currNodeQ.left:
                        pass
                    else:
                        return False        
                else:
                    return False          
            return True              
