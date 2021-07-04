"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        ret = 0
        def dfs(root, counter):
            if root is None:
                return
            counter += 1
            nonlocal ret
            if counter > ret:
                ret = counter
                
            if root.children is None:
                return
            else:
                for i in range(0, len(root.children)):
                    dfs(root.children[i], counter)

            
        dfs(root, ret)
            
        return ret
            
#runtime: O(n)
#memory: 