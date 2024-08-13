# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        #iterative sol using stack (simulating the recursive call stack)
        #post order traversal where each node visited atmost twice when its children are visited or otherwise in case of non-leaf nodes
        stack = [root]
        value = {} #maps node to value
        while stack:
            node = stack.pop()
            #leaf node
            if not node.left and not node.right:
                value[node] = (node.val == 1)
            else:
                #non-leaf nodes (children visited)
                if node.left in value:
                    if node.val == 2:
                        value[node] = value[node.left] or value[node.right]
                    else:
                        value[node] = value[node.left] and value[node.right]    
                #children not visited so need to be added togther with node to the stack
                else:
                    stack.extend([node,node.right,node.left])  

        #return the value evaluated for node from hashmap after loop ends    
        return value[root]   
