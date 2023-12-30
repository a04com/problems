class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2

        while high >= low:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
                mid = (low + high) // 2
            elif nums[mid] > target:
                high = mid - 1
                mid = (low + high) // 2
        return -1

print(Solution().search([-5], 5))
