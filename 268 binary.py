class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = sum(nums)
        m = sum(range(0, len(nums) + 1))

        return m - n
