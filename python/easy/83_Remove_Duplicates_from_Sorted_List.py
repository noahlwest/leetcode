# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        ret_head = None
        current = None
        last_val = -101
        while head:
            if ret_head is None:
                ret_head = ListNode(head.val)
                current = ret_head
                last_val = head.val
            elif head.val > last_val:
                current.next = ListNode(head.val)
                current = current.next
                last_val = head.val

            head = head.next
            
        return ret_head

#runtime: O(n)