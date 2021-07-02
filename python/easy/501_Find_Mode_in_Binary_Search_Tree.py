# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        cache = {}
        
        def dfs(root):
            if root == None:
                return
            
            dfs(root.left)
            
            nonlocal cache
            if root.val in cache:
                cache.update({root.val : cache[root.val]+1})
            else:
                cache.update({root.val : 1})
            
            dfs(root.right)
            
        dfs(root)
        
        ret = []
        max_times = 0
        for key, value in cache.items():
            if value >= max_times:
                if value == max_times:
                    ret.append(key)
                else:
                    ret.clear()
                    ret.append(key)
                    max_times = value
                    
        return ret

#runtime: O(2n) -> O(n)
#memory: O(2n?) -> O(n)