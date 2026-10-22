"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        prev = None
        new_head = None

        copy_dict = {}

        while curr:
            copy = Node(
                curr.val,
                next=curr.next,
                random=curr.random
            )

            copy_dict[curr] = copy

            if prev:
                prev.next = copy
            else:
                new_head = copy
            
            prev = copy
            curr = curr.next

        curr = new_head

        while curr:
            if curr.random:
                curr.random = copy_dict[curr.random]
            curr = curr.next

        return new_head
        