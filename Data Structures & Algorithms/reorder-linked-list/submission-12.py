# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr = head

        while curr.next and curr is not slow:
            # a->b->c
            #  f->e->d
            next1 = curr.next #b
            curr.next = prev #f
            next2 = prev.next #e
            prev.next = next1 #b
            curr = next1 #b
            prev = next2 #e

        curr.next = prev.next if prev else None
        