# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = l1
        current_node = head
        #initial addition
        sum = l1.val + l2.val
        carry_over = sum // 10
        sum = sum % 10
        head.val = sum
        l1 = l1.next
        l2 = l2.next
        
        while(l1 and l2):
            current_node.next = ListNode()
            current_node = current_node.next
            sum = l1.val + l2.val + carry_over
            carry_over = 0
            l1 = l1.next
            l2 = l2.next
            if sum >= 10:
                carry_over = sum // 10
                sum = sum % 10
                
            current_node.val = sum
            
        sum = 0
        while(l1 or l2):    
            current_node.next = ListNode()
            current_node = current_node.next
            if(l1):
                sum = l1.val + carry_over
                carry_over = 0
                l1 = l1.next
            if(l2):
                sum = l2.val + carry_over
                carry_over = 0
                l2 = l2.next
            
            if sum >= 10:
                carry_over = sum // 10
                sum = sum % 10
                
            current_node.val = sum
                
        if(carry_over > 0):
            current_node.next = ListNode()
            current_node = current_node.next
            current_node.val = carry_over
        
        return head
