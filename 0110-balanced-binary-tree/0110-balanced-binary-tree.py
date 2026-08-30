# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        difference = 0

        def dfs(root):
            nonlocal difference

            if not root: return 0

            lh = dfs(root.left)
            if lh == -1:
                return -1

            rh = dfs(root.right)
            if rh == -1:
                return -1

            difference = abs(lh - rh)

            if difference > 1:
                return -1
            
            return 1 + max(lh,rh)
        
        return dfs(root) != -1
        