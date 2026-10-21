# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0

        while curr:
            l = l + 1
            curr = curr.next

        prev = None
        curr = head

        for i in range(l - n):
            prev = curr
            curr = curr.next

        if prev:
            prev.next = curr.next
            return head
        else:
            return head.next
        