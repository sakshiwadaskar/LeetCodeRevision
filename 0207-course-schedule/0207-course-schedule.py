class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqM = {i: [] for i in range(numCourses)}
        seen = set()
        for crs, prereq in prerequisites:
            prereqM[crs].append(prereq)

        def dfs(crs):
            if crs in seen:
                return False
            if prereqM [crs] == []:
                return True
            seen.add(crs)
            for pre in prereqM[crs]:
                if not dfs(pre): 
                    return False
            seen.remove(crs)
            prereqM[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True