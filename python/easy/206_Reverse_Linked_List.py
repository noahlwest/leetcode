# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #at each step, reverse the pointer
        
        prev_node = None
        curr_node = head
        next_node = None
        
        while(curr_node is not None):
            #get pointer to next item in list
            next_node = curr_node.next
            #reverse the pointer of current item
            curr_node.next = prev_node
            #move down the list
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node

#runtime: O(n)
#memory: O(1)? 