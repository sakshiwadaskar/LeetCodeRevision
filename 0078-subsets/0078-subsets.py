class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def bfs(start, subset):


            res.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])
                bfs(i + 1, subset)
                subset.pop()

        bfs(0, subset)

        return res
        