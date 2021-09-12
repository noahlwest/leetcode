# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #do inorder traversal and verify the output
        self.last = float(-inf)
        
        def dfs(node):
            if node is None:
                return True
            accum_l = dfs(node.left)
            if node.val <= self.last:
                return False
            self.last = node.val
            accum_r = dfs(node.right)
            return True and accum_r and accum_l
            
        return dfs(root)

    #runtime: O(n)
    #memory: O(1)