# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        i = 0

        while fast:
            if i % 2 == 1:
                slow = slow.next

            fast = fast.next
            if fast == slow:
                return True
            i = i + 1

        return False
        