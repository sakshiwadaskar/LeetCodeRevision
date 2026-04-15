class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToCharMap = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl",
                        "6":"mno", "7" : "pqrs", "8": "tuv", 
                        "9": "wxyz"}
        res = []
        if not digits:
            return []

        def dfs(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            #maxL = max(len(availChars1) , len(availChars2))
            for char in numToCharMap[digits[i]]:
                path.append(char)
                dfs( i + 1, path)
                path.pop()

        dfs(0, [])
        return res

            
        