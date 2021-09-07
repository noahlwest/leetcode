# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return None
        
        ptr = head
        seen = {}
        
        while ptr is not None:
            if ptr in seen:
                return ptr
            seen.update({ptr : "_"})
            ptr = ptr.next
        return None

    #runtime: O(n)
    #memory: O(n)