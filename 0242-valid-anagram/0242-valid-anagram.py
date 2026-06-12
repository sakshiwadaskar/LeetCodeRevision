class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        map_s = {}
        for c in s:
            map_s[c] = 1 + map_s.get(c, 0)

        for c in t:
            map_s[c] = map_s.get(c, 0) - 1

            if map_s[c] < 0: return False
        return True
        