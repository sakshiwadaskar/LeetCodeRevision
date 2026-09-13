class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, total: int, path: List[int]):
            if total == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # Pruning: sorted array means all subsequent additions will also exceed target
                if total + candidates[i] > target:
                    break

                # Skip duplicate numbers at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, total + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return res