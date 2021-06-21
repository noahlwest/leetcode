# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
                
        
        #recursive:
        #if the root's left subtree matches the root's right subtree
        #if the root's right subtree matches the root's left subtree
        
        def helper(p, q):
            if(p is None and q is None):
                return True
        
            #call the function recursively:
                #if the trees have the same root
                #and the left subtrees are the same
                #and the right subtrees are the same

            if(p is not None and q is not None):
                return (p.val == q.val) and helper(p.left, q.right) and helper(p.right, q.left)
            else:
                #one != None, one == None
                return False
        
        return helper(root.left, root.right)

#runtime: O(n)