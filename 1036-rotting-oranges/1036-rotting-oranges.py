class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        q = collections.deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(len(grid))
                        and nc in range(len(grid[0]))
                        and grid[nr][nc] == 1
                    ):

                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))

            time += 1
        return time if fresh == 0 else -1

        