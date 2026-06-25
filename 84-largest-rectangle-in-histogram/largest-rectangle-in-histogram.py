class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i in xrange(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h * w)
            stack.append(i)

        heights.pop()
        return max_area