# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        #dfs, keep track of parent and grandparent
        self.total_sum = 0
        
        def dfs(self, node, parent, grandparent):
            if node is None:
                return
            if parent is None:
                dfs(self, node.left, node.val, None)
                dfs(self, node.right, node.val, None)
            else:
                if grandparent is not None and grandparent % 2 == 0:
                    self.total_sum += node.val
                dfs(self, node.left, node.val, parent)
                dfs(self, node.right, node.val, parent)
                
        dfs(self, root, None, None)
        
        return self.total_sum
                

    #runtime: O(n)
    #memory: O(1)