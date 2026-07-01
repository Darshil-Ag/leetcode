class Solution(object):
    def getMoneyAmount(self, n):
        memo = {}

        def solve(left, right):
            if left >= right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            ans = float('inf')

            for x in range(left, right + 1):
                cost = x + max(solve(left, x - 1), solve(x + 1, right))
                ans = min(ans, cost)

            memo[(left, right)] = ans
            return ans

        return solve(1, n)