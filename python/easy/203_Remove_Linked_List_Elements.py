# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        #empty list:
        if head is None:
            return head
        
        #one element list
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head
        
        #list starts with bad value
        if head.val == val:
            while head is not None and head.val == val:
                head = head.next
        if head is None:
            return None
            
            
        
        #two pointers: one to keep track of node before deletion, one for traversal node
        prev = head
        cur = head.next
        
        marked_for_deletion = False
        
        while cur is not None:
            if cur.val != val and marked_for_deletion == False:
                #just move forward looking for bad nodes
                prev = cur
                cur = cur.next
            elif cur.val != val and marked_for_deletion == True:
                #awaiting deletion, connect prev to cur so we "delete" the bad nodes
                prev.next = cur
                prev = cur
                cur = cur.next
                marked_for_deletion = False
            elif cur.val == val and marked_for_deletion == False:
                #mark it for deletion, then start traversing 
                marked_for_deletion = True
                cur = cur.next
            elif cur.val == val and marked_for_deletion == True:
                #just move forward to skip over bad nodes
                cur = cur.next
                
        prev.next = None
                
        return head
        
#runtime: O(n)
#memory: O(1) I think, I just use 2 "pointers" and a bool