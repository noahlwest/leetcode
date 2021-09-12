# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.sum = 0
        
        def dfs(self, node):
            if node is None:
                return
            dfs(self, node.left)
            if node.val >= low and node.val <= high:
                self.sum += node.val
            
            dfs(self, node.right)
        
        dfs(self, root)

        return self.sum

    #runtime: O(n)
    #memory: O(1)