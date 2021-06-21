# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        #keep track of maximum depth
        #call with tracker+1
        #on each iteration, keep max(tracker, maximum)
        #return tracker-1
        
        maximum = 0
            
        def dfs_helper(root, counter):
            nonlocal maximum
            if root is None:
                if(counter > maximum):
                    maximum = counter
                return
            
            dfs_helper(root.left, counter + 1)
            dfs_helper(root.right, counter + 1)
            
            return counter - 1
        
        dfs_helper(root, 0)
        
        return maximum
    
#runtime: O(n)