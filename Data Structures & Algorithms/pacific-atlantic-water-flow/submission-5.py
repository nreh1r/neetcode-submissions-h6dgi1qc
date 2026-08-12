class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		rows, cols = len(heights), len(heights[0])
		pac, atl = set(), set()
		res = []
		
		def dfs(row, col, visited, prev_height):
			if (
				row < 0 or col < 0 or
				row >= rows or col >= cols or
				(row, col) in visited or
				heights[row][col] < prev_height
			):
				return
			
			visited.add((row, col))
			dfs(row + 1, col, visited, heights[row][col])
			dfs(row - 1, col, visited, heights[row][col])
			dfs(row, col + 1, visited, heights[row][col])
			dfs(row, col - 1, visited, heights[row][col])
		
		for c in range(cols):
			dfs(0, c, pac, heights[0][c])
			dfs(rows - 1, c, atl, heights[rows - 1][c])
		
		for r in range(rows):
			dfs(r, 0, pac, heights[r][0])
			dfs(r, cols - 1, atl, heights[r][cols - 1])
			
		for r in range(rows):
			for c in range(cols):
				if (r, c) in pac and (r, c) in atl:
					res.append([r, c])
		
		return res