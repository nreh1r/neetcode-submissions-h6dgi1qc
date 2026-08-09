class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0
		
		rows, cols = len(grid), len(grid[0])
		visited = set()
		self.res = 0
		
		def bfs(row, col):
			queue = deque([(row, col)])
			
			while queue:
				r, c = queue.popleft()
				
				if (
					r < 0 or c < 0 or
					r >= rows or c >= cols or
					(r, c) in visited or
					grid[r][c] == "0"
				):
					continue
				
				visited.add((r, c))
				
				queue.append((r + 1, c))
				queue.append((r - 1, c))
				queue.append((r, c + 1))
				queue.append((r, c - 1))
		
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1" and (r, c) not in visited:
					bfs(r, c)
					self.res += 1
		
		return self.res