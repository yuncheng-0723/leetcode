# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        inputS = ""
        while head:
            inputS+= str(head.val)
            head = head.next
        return True if inputS == inputS[::-1] else False