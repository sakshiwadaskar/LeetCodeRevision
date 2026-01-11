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
        oldToCopy = {None: None}

        while curr:
            newCurr = Node(curr.val)
            oldToCopy[curr] = newCurr
            curr = curr.next

        curr = head
        while curr:
            newCurr = oldToCopy[curr]
            newCurr.next = oldToCopy[curr.next]
            newCurr.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
        