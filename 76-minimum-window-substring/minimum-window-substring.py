class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        missing = len(t)
        left = start = end = 0

        for right in xrange(len(s)):
            if s[right] in need:
                if need[s[right]] > 0:
                    missing -= 1
                need[s[right]] -= 1

            while missing == 0:
                if end == 0 or right - left + 1 < end - start:
                    start, end = left, right + 1

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        missing += 1
                left += 1

        return s[start:end]