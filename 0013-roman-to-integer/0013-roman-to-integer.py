class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanToInt[s[i]] < romanToInt[s[i + 1]]:
                total -= romanToInt[s[i]]
            else:
                total += romanToInt[s[i]] 
        return total      