from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])
        res = []

        if window == p_count:
            res.append(0)

        for i in range(len(p), len(s)):
            window[s[i]] += 1
            window[s[i - len(p)]] -= 1

            if window[s[i - len(p)]] == 0:
                del window[s[i - len(p)]]

            if window == p_count:
                res.append(i - len(p) + 1)

        return res