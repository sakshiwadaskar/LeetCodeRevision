class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_f = 0
        count_map = {} # char - > count
        res = 0

        for r in range(len(s)):
            count_map[s[r]] = 1 + count_map.get(s[r], 0)
            max_f = max(max_f, count_map[s[r]])

            while ( r - l + 1) - max_f  > k:
                count_map[s[l]] -= 1
                l += 1

            res = max(res,  (r - l + 1))
            r += 1
        return res
        