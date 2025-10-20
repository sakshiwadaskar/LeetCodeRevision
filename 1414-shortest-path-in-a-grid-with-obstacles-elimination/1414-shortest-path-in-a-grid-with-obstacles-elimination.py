import collections

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        q = collections.deque([(0, 0, 0, k)])  # (steps, r, c, remaining eliminations)
        visited = set([(0, 0, k)])

        while q:
            steps, r, c, e = q.popleft()

            # Reached goal
            if (r, c) == (rows - 1, cols - 1):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                newE = e - grid[nr][nc]  # use one elimination if obstacle
                if newE < 0:
                    continue  # can’t pass obstacle
                if (nr, nc, newE) not in visited:
                    visited.add((nr, nc, newE))
                    q.append((steps + 1, nr, nc, newE))

        return -1
