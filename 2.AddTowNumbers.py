# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        num3 = ""
        returnLinkList = None

        while l1:
            num1 = f"{l1.val}{num1}"
            l1 = l1.next
        while l2:
            num2 = f"{l2.val}{num2}"
            l2 = l2.next
        num3 = reversed(str(int(num1) + int(num2)))
        for s in num3:
            new_node = ListNode(int(s))

            if not returnLinkList:
               returnLinkList = new_node
            else:
                current = returnLinkList
                while current.next:
                    current = current.next
                current.next = new_node
        return returnLinkList
