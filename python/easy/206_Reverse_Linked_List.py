# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #recursive:
        #go from top to bottom of list
        #once at bottom of list:
            #add the last value to the end of the current list
        
        ret_head = None
        cur = None
        
        def helper(node):
            if node is None:
                return
            #navigate down the list
            helper(node.next)
            #at the bottom of the list: start appending values to ret
            nonlocal ret_head, cur
            if ret_head is None:
                ret_head = ListNode(node.val)
                cur = ret_head
            else:
                cur.next = ListNode(node.val)
                cur = cur.next
        
        helper(head)
        return ret_head
#runtime: O(n)
#memory: O(n)? 