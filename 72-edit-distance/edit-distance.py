class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in xrange(m + 1)]

        for i in xrange(m + 1):
            dp[i][0] = i

        for j in xrange(n + 1):
            dp[0][j] = j

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]