class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        minHeap = [(0, 0, 0)]

        while minHeap:
            w1, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue

            if (r, c) == (rows - 1, cols - 1):
                return w1
            
            visit.add((r, c))

            for dr,dc in directions:
                nr, nc = r + dr, c +  dc
                if (
                    nr < 0 or nc < 0 or
                    nr >= rows or nc >= cols or
                    (nr, nc) in visit
                ):
                    continue
                newDiff = max (w1, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minHeap, [newDiff, nr, nc])
        return 0







        