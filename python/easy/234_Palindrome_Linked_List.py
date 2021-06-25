# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #read linked list into a string
        #copy and reverse the string
        #check if they're the same
        string = ""
        while head is not None:
            string += str(head.val)
            head = head.next
            
        return string[::-1] == string
#runtime: O(n) (slow though)