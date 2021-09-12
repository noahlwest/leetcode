# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.target = target
        self.path = []
        
        def find_original(self, node, path):
            if node is None:
                return
            if node == self.target:
                self.path = path
                return
            find_original(self, node.left, path + ['L'])
            find_original(self, node.right, path + ['R'])
            if len(path) > 0:
                path.pop()
            
        find_original(self, original, [])
            
        curr = cloned
        for instruction in self.path:
            if instruction == 'L':
                curr = curr.left
            if instruction == 'R':
                curr = curr.right
            
        return curr

    #runtime: O(n)
    #memory: O(log n)