class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            ind = abs(num)-1
            if nums[ind]<0:
                res.append(abs(num))
            else:
                nums[ind]=-nums[ind]
        return res
        