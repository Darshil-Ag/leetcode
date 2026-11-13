
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        END = "#"
        root = {}

        # Insert a word into the Trie
        def insert(word):
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[END] = True

        # Check whether word can be formed using Trie words
        def can_form(word):
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(n):
                if not dp[i]:
                    continue

                node = root

                for j in range(i, n):
                    ch = word[j]

                    if ch not in node:
                        break

                    node = node[ch]

                    if END in node:
                        dp[j + 1] = True

            return dp[n]

        result = []

        # Process shorter words first
        words.sort(key=len)

        for word in words:
            if can_form(word):
                result.append(word)

            # Insert only after checking
            insert(word)

        return result
