# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        #bfs
        ret = []
        
        q = []
        q.append(root)
        
        while len(q) > 0:
            curr_level = []
            length = len(q)
            for i in range(0, length):
                curr_node = q.pop(0)
                curr_level.append(curr_node.val)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            ret.append(curr_level)
        
        return ret