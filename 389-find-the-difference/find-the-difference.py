class Solution(object):
    def findTheDifference(self, s, t):
        x = 0

        for ch in s:
            x ^= ord(ch)

        for ch in t:
            x ^= ord(ch)

        return chr(x)