class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final = []
        temp = []
        for i in range(len(nums)):
            if target - nums[i] in temp:
                final.append(i)
                break
            else:
                temp.append(nums[i])
        diff = target - nums[final[0]]
        for i in range(len(nums)):
            if nums[i]==diff:
                final.append(i)
                break
        return final
        
                
        