# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        #inorder: left -> root -> right
        if root is None:
            return []
        
        def dfs_helper(root, ret):
            if root is None:
                return
            dfs_helper(root.left, ret)
            ret.append(root.val)
            dfs_helper(root.right, ret)
            return ret
        
        return dfs_helper(root, [])

#runtime: O(n)