class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # Requirement for the skip logic

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Rule 2: Skip duplicates at the same recursive level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Rule 1: We use total + candidates[i] 
                # Optimization: if it's too big, stop (because it's sorted)
                if total + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                # Note: we pass 'i + 1' so we don't reuse the SAME element
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res