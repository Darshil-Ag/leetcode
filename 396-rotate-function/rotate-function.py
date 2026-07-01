class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        ans = f

        for i in range(n - 1, 0, -1):
            f = f + total - n * nums[i]
            ans = max(ans, f)

        return ans