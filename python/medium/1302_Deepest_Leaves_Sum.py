# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        #iterative BFS, adding up sums at each layer, returning sum of last layer
        queue = deque()
        queue.append(root)
        sums = []
        
        while len(queue) > 0:
            length = len(queue)
            this_layer_sum = 0
            for i in range(0, length):
                node = queue.popleft()
                this_layer_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            sums.append(this_layer_sum)
            
        return sums[len(sums)-1]

    #memory: O(n)
    #runtime: O(n)