# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        #2 pointers: 1 initial pointer, 1 that stays n+1 nodes behind
        p1 = head
        for i in range(0, n):
            p1 = p1.next

        #if p1 is off the list: remove the head
        if p1 is None:
            return head.next
        
        #otherwise: stay n+1 spaces behind
        p1 = p1.next
        p2 = head
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
            
        #"delete" the node
        p2.next = p2.next.next
        
        return head

#runtime: O(n)
#memory: O(1)