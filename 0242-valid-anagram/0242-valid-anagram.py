class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        map_s = {}
        for i in range(len(s)):
            map_s[s[i]] = 1 + map_s.get(s[i], 0)

        for c in t:
            map_s[c] = map_s.get(c, 0) - 1

            if map_s[c] < 0: return False
        return True
        