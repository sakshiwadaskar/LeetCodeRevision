class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(start, total, path):

            if target == total:
                res.append(path.copy())

            for i in range(start, len(candidates)):

                if candidates[i] + total > target:
                    break

                # Skip duplicate numbers at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                dfs(i + 1, candidates[i] + total, path)
                path.pop()

        dfs(0, 0, path)
        return res
        