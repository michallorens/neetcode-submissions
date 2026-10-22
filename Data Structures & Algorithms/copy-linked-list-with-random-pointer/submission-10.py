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
        copies = {None: None}

        while curr:
            if curr not in copies:
                copies[curr] = Node(curr.val)
            if curr.next not in copies:
                copies[curr.next] = Node(curr.next.val)
            if curr.random not in copies:
                copies[curr.random] = Node(curr.random.val)
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next

        return copies[head]
        