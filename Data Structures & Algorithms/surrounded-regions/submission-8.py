class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            surrounded = True
            region = []

            while queue:
                r, c = queue.popleft()

                region.append((r, c))

                if (
                    r == 0 or r == rows - 1 or
                    c == 0 or c == cols - 1
                ):
                    surrounded = False
                
                for dr, dc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]:
                    if (
                        0 <= dr < rows and
                        0 <= dc < cols and
                        board[dr][dc] == "O" and
                        (dr, dc) not in visited
                    ):
                        queue.append((dr, dc))
                        visited.add((dr, dc))

            if surrounded:
                for row, col in region:
                    board[row][col] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    bfs(r, c)