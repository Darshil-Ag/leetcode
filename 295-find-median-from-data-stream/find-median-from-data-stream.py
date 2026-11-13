
import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # Max Heap (negative values)
        self.large = []  # Min Heap

    def addNum(self, num):
        # Add to smaller half
        heapq.heappush(self.small, -num)

        # Move largest of smaller half to larger half
        largest = -heapq.heappop(self.small)
        heapq.heappush(self.large, largest)

        # Balance heaps: smaller half can have one extra
        if len(self.large) > len(self.small):
            smallest = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0
