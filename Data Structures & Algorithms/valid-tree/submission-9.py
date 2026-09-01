class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(n)}

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for edge in adj_list[node]:
                if edge == prev:
                    continue
                
                if not dfs(edge, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n