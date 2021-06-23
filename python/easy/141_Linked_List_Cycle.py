# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None:
            return False
        
        tortoise = head
        hare = head.next
        
        while True:
            if tortoise == hare:
                return True
            if hare is None or hare.next is None:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
                
        return False

#runtime: O(n)? worst case is that it hits 2n, I think