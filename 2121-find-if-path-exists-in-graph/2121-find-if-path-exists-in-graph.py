class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            for neigh in graph[i]:
                if neigh not in seen:
                    seen.add(neigh)
                    if dfs(neigh):
                        return True
            return False
        
        return dfs(source)
        