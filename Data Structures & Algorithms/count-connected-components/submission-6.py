class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        print(adj_list)

        def dfs(node, prev):
            print("node: ", node)
            if node in visited:
                return False
            
            visited.add(node)

            for edge in adj_list[node]:
                if edge == prev:
                    continue
                
                dfs(edge, node)
                    
            
            return True
            
        curr_count = 0
        curr_explored = len(visited)
        for node in range(n):
            print("call", node)
            dfs(node, -1)
            if len(visited) > curr_explored:
                curr_count += 1
                curr_explored = len(visited)
        
        return curr_count
        
