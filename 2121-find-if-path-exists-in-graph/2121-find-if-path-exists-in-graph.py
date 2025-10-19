class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited.add(source)

        q = collections.deque()
        q.append(source)

        while q:
            node = q.popleft()
            if node == destination:
                return True

            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
        return False