# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Case 1 : Leaf node (i.e no left or right child)
        #Case 2 : either of left or right child only
        #Case 3 : both left and right child of a node 
        #Inorder traversal of BST results in sorted array  ---> e.g 2,3,4,5,6,7
        #so we have two options either find min from right subtree or max from left subtree to replace the key node given 
        #and then finally delete for e.g the min node value from right subtree we used to replace key node by recursively calling delete node functions

        if not root:        #base case
            return root
        if key > root.val:  #search right subtree
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:  #search left subtree
            root.left = self.deleteNode(root.left,key)
        else:               #we found the node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                #finding min from right subtree to replace it with key node val we found
                #guarnateed to have no left chlid atleast
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                #after replacing value calling deleteNode function recursively to delete the duplicate
                root.right = self.deleteNode(root.right,curr.val)
        return root                    

