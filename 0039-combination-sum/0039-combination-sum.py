class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res, path = [], []
        candidates.sort()

        def dfs(start, path, curSum):

            if curSum == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):

                if curSum + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i, path, curSum + candidates[i])
                path.pop()

        dfs(0, path, 0)
        return res
        