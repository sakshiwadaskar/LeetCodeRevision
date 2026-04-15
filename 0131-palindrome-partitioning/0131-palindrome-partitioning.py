class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i , path):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for n in range(i, len(s)):
                substring= s[i:n+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    dfs(n + 1, path)
                    path.pop()

        dfs(0, [])
        return res