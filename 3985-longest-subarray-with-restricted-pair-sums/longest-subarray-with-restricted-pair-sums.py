class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        freq = [0] * 501
        left = 0
        max_len = 0
        
        def is_valid_with(val):
            # 1) Check if two elements in the window sum to val
            for x in range(1, 501):
                if freq[x] > 0:
                    y = val - x
                    if 1 <= y <= 500 and freq[y] > 0:
                        if x == y:
                            if freq[x] >= 2:
                                return False
                        else:
                            return False
            
            # 2) Check if an element in the window plus val equals another element in the window (x + val == z)
            for x in range(1, 501):
                if freq[x] > 0:
                    z = x + val
                    if z <= 500 and freq[z] > 0:
                        return False
                        
            return True

        for right in range(n):
            val = nums[right]
            while not is_valid_with(val):
                freq[nums[left]] -= 1
                left += 1
            freq[val] += 1
            max_len = max(max_len, right - left + 1)
            
        return max_len