class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, subset= [], []

        def dfs(subset):

            if len(subset) == len(nums):
                res.append(subset.copy())
                return res

            for choice in nums:
                if choice in subset:
                    continue

                subset.append(choice)
                dfs(subset)
                subset.pop()

        dfs(subset)
        return res