# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leaf_sum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs_sum(root, 0)
        return self.leaf_sum
        
        
    def dfs_sum(self, node, curr_sum):
        if node is None:
            return
        
        curr_sum *= 10
        curr_sum += node.val
        
        if node.left is None and node.right is None:
            self.leaf_sum += curr_sum
            return
        
        self.dfs_sum(node.left, curr_sum)
        self.dfs_sum(node.right, curr_sum)

    #runtime: O(n)
    #memory: O(1) (if you disregard call stack)