# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #if l1 is empty and l2 is not empty:
            #return l2
        #if l1 is not empty and l2 is empty:
            #return l1
        #otherwise:
        #while l1 is not empty or l2 is not empty:
            #merge the lists:
                
            
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None
        
        head = None
        
        #both lists not empty: create the return list
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        current = head
        
        while l1 or l2:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    current.next = l1
                    current = current.next
                    l1 = l1.next
                else:
                    current.next = l2
                    current = current.next
                    l2 = l2.next
            elif l1:
                current.next = l1
                break
            else:
                current.next = l2
                break
                
        return head
      
#runtime: O(n+m) = O(n)