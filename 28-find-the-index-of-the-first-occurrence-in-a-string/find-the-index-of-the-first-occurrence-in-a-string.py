class Solution(object):
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
                
        return -1