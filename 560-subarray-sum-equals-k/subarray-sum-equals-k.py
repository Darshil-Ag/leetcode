class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = {0:1}
        count = 0
        summ = 0
        for i in nums:
            summ+=i
            if summ-k in mapp:
                count+=mapp[summ-k]
            mapp[summ]=mapp.get(summ,0)+1
        return count
        