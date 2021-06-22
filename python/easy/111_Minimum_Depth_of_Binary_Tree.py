# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        minimum = 100001
            
        def dfs_helper(root, counter):
            nonlocal minimum
            if root is None:
                return
            if root.left is None and root.right is None:
                if(counter < minimum):
                    minimum = counter
                return
            
            dfs_helper(root.left, counter + 1)
            dfs_helper(root.right, counter + 1)
            
            return counter - 1
        
        dfs_helper(root, 1)
        
        return minimum

#runtime: O(n)