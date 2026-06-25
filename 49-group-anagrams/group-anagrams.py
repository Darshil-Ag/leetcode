class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
            
        return list(anagrams.values())