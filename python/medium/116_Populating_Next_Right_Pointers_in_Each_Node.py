"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            prev = None
            curr = None
            length = len(q)
            for i in range(0, length):
                curr = q.popleft()
                if prev is not None:
                    prev.next = curr
                if curr is not None:
                    q.append(curr.left)
                    q.append(curr.right)
                prev = curr
                
        return root
                
    #runtime: O(n)
    #memory: O(n)