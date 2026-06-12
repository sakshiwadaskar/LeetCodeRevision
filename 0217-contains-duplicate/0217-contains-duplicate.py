class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()

        for n in nums:
            if n in dupSet:
                return True
            else:
                dupSet.add(n)
        return False