class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        returnn = 0
        total = sum(nums)
        summ = 0
        n =int(len(nums)/2)
        for i in range(n):
            summ+=nums[i]
        j = n
        i = 0
        for k in range(len(nums)):
            end = j+k
            start = i+k
            if end >= len(nums):
                end = end % len(nums)
            if start >= len(nums):
                start = start % len(nums)
            summ+=nums[end]
            summ-=nums[start]
            if summ > total - summ:
                returnn +=1
        return returnn
