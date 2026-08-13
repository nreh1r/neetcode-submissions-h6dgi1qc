class Solution:
	def solve(self, board: List[List[int]]) -> None:
		rows, cols = len(board), len(board[0])
		
		def bfs():
			queue = deque()
			
			for r in range(rows):
				for c in range(cols):
					if (
						(r == 0 or r == rows - 1 or
						c == 0 or c == cols - 1) and
						board[r][c] == "O"
					):
						queue.append((r, c))
			
			while queue:
				r, c = queue.popleft()
				board[r][c] = "T"
				
				for dr, dc in [
					(r + 1, c),
					(r - 1, c),
					(r, c + 1),
					(r, c - 1)
				]:
					if (
						0 <= dr < rows and
						0 <= dc < cols and
						board[dr][dc] == "O"
					):
						queue.append((dr, dc))
		bfs()
		for r in range(rows):
			for c in range(cols):
				if board[r][c] == "O":
					board[r][c] = "X"
				elif board[r][c] == "T":
					board[r][c] = "O"