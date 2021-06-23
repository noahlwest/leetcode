# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None:
            return False
        
        seen = {}
        
        while head is not None:
            if id(head) in seen:
                return True
            else:
                seen.update({id(head) : "_"})
            head = head.next
                
        return False

#runtime: O(n)