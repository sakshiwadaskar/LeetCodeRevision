class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res= [], []

        def dfs(openN, closeN):
            if openN == closeN == n:
               res.append("".join(stack))

            if openN < n:
                stack.append("(")
                dfs(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(")")
                dfs(openN , closeN + 1)
                stack.pop()

        dfs(0,0)
        return res