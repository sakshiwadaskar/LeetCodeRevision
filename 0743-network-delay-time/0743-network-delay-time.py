class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        visited = set()

        for u, v, w in times:
            edges[u].append((v,w))

        minHeap = [(0, k)]
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            visited.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                newDist = w1 + w2

                if n2 not in visited:
                    heapq.heappush(minHeap, (newDist, n2))
        return t if len(visited) == n else -1

        