
class Solution(object):
    def singleNumber(self, nums):
        xor = 0

        # Step 1: XOR all numbers
        for num in nums:
            xor ^= num

        # Step 2: Get rightmost set bit
        diff = xor & -xor

        # Step 3: Separate numbers into two groups
        a = 0
        b = 0

        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]
