# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #do inorder traversal and verify the output
        self.arr = []
        
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        for i in range(1, len(self.arr)):
            if self.arr[i] <= self.arr[i-1]:
                return False
            
        return True

    #runtime: O(n)
    #memory: O(n)