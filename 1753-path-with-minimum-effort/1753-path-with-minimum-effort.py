class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows , cols = len(heights), len(heights[0])

        heap = [[0,0,0]]
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
                maxDiff = max( diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap,[maxDiff, nr, nc])
        return 0
