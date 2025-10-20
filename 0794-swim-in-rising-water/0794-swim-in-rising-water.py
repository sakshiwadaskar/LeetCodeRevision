class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])

        heap = [[grid[0][0], 0, 0]]
        visited = set()
        directions = [[0,1],[0,-1], [1,0], [-1,0]]

        while heap:
            diff, r, c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (rows - 1 , cols - 1):
                return diff
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols 
                    or (nr,nc) in visited):
                    continue
                heapq.heappush(heap,[max(diff,grid[nr][nc]), nr, nc])
        return 0
        