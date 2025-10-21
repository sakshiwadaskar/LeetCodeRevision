class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = 0
        visited = [False] * len(strs)

        def dfs(i):
            visited[i] = True

            for j in range(len(strs)):
                if visited[j]: continue
                if isSimilar(strs[i], strs[j]):
                    dfs(j)

        def isSimilar(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: 
                    count += 1
            return count == 2 or count == 0


        for i in range(len(strs)):
            if not visited[i]:
                dfs(i)
                groups += 1
        return groups
        