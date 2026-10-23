# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l3 = head
        carry = 0

        while l1 and l2:
            node = ListNode()
            node.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l3.next = node
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        l = l1 if l1 else l2

        while l:
            node = ListNode()
            node.val = (l.val + carry) % 10
            carry = (l.val + carry) // 10
            l3.next = node
            l3 = l3.next
            l = l.next

        if carry:
            l3.next = ListNode(val=carry)

        return head.next


        