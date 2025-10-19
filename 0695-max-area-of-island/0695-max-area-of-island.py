class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0

        def dfs(r,c):
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1],[0,-1]]
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows) and 
                    nc in range(cols) and
                    grid[nr][nc] == 1 and
                    (nr, nc) not in visited):

                    res += dfs(nr, nc)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, dfs(r,c)) 

        return area