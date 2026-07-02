class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:
            return False

        width = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket = num // width

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True

            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[old // width]

        return False