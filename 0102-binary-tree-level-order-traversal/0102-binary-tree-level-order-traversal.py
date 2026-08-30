# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                front = q.popleft()
                level.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)            
            if level:
                res.append(level)

            return res

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        res = []

        while q:
            q_len = len(q)
            level = []

            for _ in range(q_len):
                front = q.popleft()
                level.append(front.val)

                # Nest child additions inside the loop
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

            res.append(level)

        return res
