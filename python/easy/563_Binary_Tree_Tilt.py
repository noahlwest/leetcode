# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        ret = 0
        def dfs_tilt(root):
            if root is None:
                return 0
            nonlocal ret
            ret += abs(dfs_sum(root.left) - dfs_sum(root.right))
            dfs_tilt(root.left)
            dfs_tilt(root.right)
        
        def dfs_sum(root):
            if root is None:
                return 0
            return root.val + dfs_sum(root.left) + dfs_sum(root.right)
        
        if root is None:
            return 0
        
        dfs_tilt(root)
            
        return ret

#runtime: O(n^2?)
#memory: O(1) + stack growth = O(n?)