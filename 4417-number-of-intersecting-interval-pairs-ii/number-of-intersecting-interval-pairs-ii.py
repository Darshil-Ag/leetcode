import heapq

class Solution:
    def countIntersectingIntervals(self, nums: list[list[int]]) -> int:
        heap = []
        nums.sort()
        heapq.heappush(heap, nums[0][1])
        sol = 0
        n = len(nums)

        for i in range(1, n):
            while heap and heap[0] < nums[i][0]:
                heapq.heappop(heap)

            sol += len(heap)
            heapq.heappush(heap, nums[i][1])

        return sol