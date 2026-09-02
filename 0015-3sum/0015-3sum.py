class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):

            if nums[i] > 0: break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1 , len(nums) - 1
            threeSum = nums[i]

            while l < r:
                if threeSum + nums[l] + nums [r] > 0:
                    r -= 1

                elif threeSum + nums[l] + nums [r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+= 1

                    while nums[l] == nums[l -1 ] and l < r:
                        l+= 1
        return res
        