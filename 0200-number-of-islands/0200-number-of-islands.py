class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def bfs(r,c):
            seen.add((r,c))
            q = collections.deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0,1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == "1" and (nr,nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1

        return islands
        