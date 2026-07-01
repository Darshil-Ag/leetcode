class Solution(object):
    def countLessEqual(self, matrix, mid):
        n = len(matrix)
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1

        return count

    def kthSmallest(self, matrix, k):
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            mid = low + (high - low) // 2

            if self.countLessEqual(matrix, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low