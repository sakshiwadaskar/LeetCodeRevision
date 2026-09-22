from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # If either the start or end cell is
        # blocked, no path can ever exist
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # Queue holds (row, col, path length so far)
        queue = deque([(0, 0, 1)])
        visit = set()
        visit.add((0, 0))

        # All 8 directions, since diagonal
        # moves are allowed here
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),           (0,1),
                      (1,-1),  (1,0),  (1,1)]

        while queue:
            r, c, length = queue.popleft()

            # Reached the bottom-right cell,
            # this is the shortest path length
            if (r, c) == (n - 1, n - 1):
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip if out of bounds, blocked,
                # or already visited
                if (nr < 0 or nr >= n or
                    nc < 0 or nc >= n or
                    grid[nr][nc] == 1 or
                    (nr, nc) in visit):
                    continue

                visit.add((nr, nc))
                queue.append((nr, nc, length + 1))

        # Queue emptied without reaching the
        # bottom-right cell, so no path exists
        return -1