class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node):
            for edge in adj_list[node]:
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge)
        
        res = 0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        
        return res