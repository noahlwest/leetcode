# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.ret = []
        
        def dfs(node, path):
            if node is None:
                return
            if path:
                path += "->" + str(node.val)
            else:
                path += str(node.val)
            if node.left is None and node.right is None:
                self.ret.append(path)
                return
            dfs(node.left, path)
            dfs(node.right, path)
            
        dfs(root, "")
        return self.ret

    #runtime: O(n)
    #memory: O(n)?