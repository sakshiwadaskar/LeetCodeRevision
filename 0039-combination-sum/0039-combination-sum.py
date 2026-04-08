class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(start, path, total):
            if total == target:
                res.append(path[:])
                return

            for j in range(start, len(nums)):

                if nums[j] + total > target:
                    continue

                path.append(nums[j])
                backtracking(j, path, nums[j] + total)
                path.pop()

        backtracking(0, [], 0)
        return res