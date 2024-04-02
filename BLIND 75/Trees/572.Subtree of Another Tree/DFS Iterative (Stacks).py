# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #DFS Iterative (using stacks)
        stack = [root]
        
        while stack:
            currNode = stack.pop()
            #checking that from this node onwards that subtree has same descendants or not i.e "same tree" algorithm is used
            if currNode.val == subRoot.val:
                stackP = [currNode]
                stackQ = [subRoot]
                
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
                            break       
                        if currNodeP.left and currNodeQ.left:
                            stackP.append(currNodeP.left)
                            stackQ.append(currNodeQ.left)
                        elif not currNodeP.left and not currNodeQ.left:
                            pass
                        else:
                            break
                    else:
                        break        
                #if while loop doesnot terminate with break statement then both are same tree from that particular node onwards
                else:
                    return True
            
            #we keep adding and removing from stack node by node
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)  
        
        return False

