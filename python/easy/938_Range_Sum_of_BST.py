# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.nums = []
        
        def dfs(self, node):
            if node is None:
                return
            dfs(self, node.left)
            self.nums.append(node.val)
            dfs(self, node.right)
        
        dfs(self, root)

        filtered_nums = filter(lambda x: x >= low and x <= high, self.nums)

        return sum(filtered_nums)

#runtime: O(n)
#memory: O(n)