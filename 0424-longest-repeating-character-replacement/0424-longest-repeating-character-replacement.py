class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        maxF = 0
        res= 0
        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            maxF = max(maxF, charMap[s[r]])
            if ( r - l + 1) - maxF > k:
                charMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
        