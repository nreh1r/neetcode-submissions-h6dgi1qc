class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
				
				dfs(edge, node)
			
			return True
		
		curr_count = 0
		curr_length = len(visited)
		for node in range(n):
			dfs(node, -1)
			if len(visited) > curr_length:
				curr_count += 1
				curr_length = len(visited)
		
		return curr_count