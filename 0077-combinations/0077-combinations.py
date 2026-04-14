class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(start, path):

            if k == len(path):
                res.append(path.copy())
                return
            
            for i in range(start, n + 1):

                if i > start and i == i - 1:
                    continue
                
                path.append(i)
                backtracking(i+1, path)
                path.pop()

        
        backtracking(1, [])
        return res
