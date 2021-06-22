# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if root is None:
            return False
            
        matchFound = False
        sum = 0
            
        def dfs_helper(root):
            nonlocal matchFound
            if matchFound:
                return
            
            if root is None:
                return
            
            nonlocal sum
            sum += root.val
            
            if root.left is None and root.right is None:
                print(sum == targetSum)
                if sum == targetSum:
                    matchFound = True
                    return
                
            dfs_helper(root.left)
            dfs_helper(root.right)
            sum -= root.val
        
        dfs_helper(root)
        
        return matchFound

#runtime: O(n)