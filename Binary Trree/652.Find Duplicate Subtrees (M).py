# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        #using defaultdict so that it does not generate keyError if a key doesnot exist
        #key must be immutable structure
        subtrees = defaultdict(list)
        #preorder DFS recursive algorithm
        def dfs(node):
            #base case so that serialization of every subtree is unique
            if not node:
                return 'null' 
            serialized_subtree = ','.join([str(node.val),dfs(node.left),dfs(node.right)])
            #i.e we have found a duplicate and we need to append it to res only once
            if len(subtrees[serialized_subtree]) == 1:
                res.append(node)
            subtrees[serialized_subtree].append(node)
            return serialized_subtree    
        dfs(root)      
        return res
        
