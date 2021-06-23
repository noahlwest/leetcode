# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        
        def dfs_helper(root, ret):
            if root is None:
                return
            dfs_helper(root.left, ret)
            dfs_helper(root.right, ret)
            ret.append(root.val)
            
        dfs_helper(root, ret)
        
        return ret

#runtime: O(n)