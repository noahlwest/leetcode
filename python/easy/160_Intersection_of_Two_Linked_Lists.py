# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        #go fully to the end of one list, then fully to the end of the other one
        #if any pointers match, they intersect
        seen = {}
        
        if headA is None or headB is None:
            return None
        
        while headA is not None:
            seen.update({id(headA) : "_"})
            headA = headA.next
            
        while headB is not None:
            if id(headB) in seen:
                return headB
            headB = headB.next
            
        return None

#runtime: O(n + m)
#memory: O(n)