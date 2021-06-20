# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        #both are None; return true
        if(p is None and q is None):
            return True
        
        def helper(p, q):
            if(p is None and q is None):
                return True
        
            #call the function recursively:
                #if the trees have the same root
                #and the left subtrees are the same
                #and the right subtrees are the same

            if(p is not None and q is not None):
                return (p.val == q.val) and helper(p.left, q.left) and helper(p.right, q.right)
            else:
                #one != None, one == None
                return False
        
        return helper(p, q)

#runtime: O(2n) -> O(n)