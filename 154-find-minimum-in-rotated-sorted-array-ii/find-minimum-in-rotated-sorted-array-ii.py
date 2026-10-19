class Solution:
    def findMin(self, nums: list[int]) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            mid = (i + j) // 2

            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                j -= 1

        return nums[i]