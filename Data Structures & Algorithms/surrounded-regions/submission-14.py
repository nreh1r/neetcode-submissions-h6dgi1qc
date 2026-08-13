class Solution:
	def solve(self, board: List[List[int]]) -> None:
		rows, cols = len(board), len(board[0])
		
		def dfs(row, col):
			if (
				row < 0 or col < 0 or
				row == rows or col == cols
				or board[row][col] != "O"
			):
				return
			
			board[row][col] = "T"

			dfs(row + 1, col)
			dfs(row - 1, col)
			dfs(row, col + 1)
			dfs(row, col - 1)
		
		for r in range(rows):
			for c in range(cols):
				if (
					(r == 0 or r == rows - 1 or
					c == 0 or c == cols - 1) and
					board[r][c] == "O"
				):
					dfs(r, c)
					
		for r in range(rows):
			for c in range(cols):
				if board[r][c] == "O":
					board[r][c] = "X"
				
				if board[r][c] == "T":
					board[r][c] = "O"