"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtoNew = {}
        oldtoNew[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in oldtoNew:
                    copynei = Node(nei.val)
                    oldtoNew[nei] = copynei
                    q.append(nei)
                oldtoNew[curr].neighbors.append(oldtoNew[nei])

        return oldtoNew[node]