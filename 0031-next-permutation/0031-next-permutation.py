class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = -1

        # Step 1: Find the break-point (first index from the right where nums[i] < nums[i + 1])
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # If no break-point exists, array is in descending order; reverse to get the smallest permutation
        if ind == -1:
            nums.reverse()
            return

        # Step 2: Find the element from the right greater than nums[ind], and swap them
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 3: Reverse the remaining suffix to make it lexicographically smallest
        nums[ind + 1:] = reversed(nums[ind + 1:])