class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        self.res = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = "0"

            while queue:
                r, c = queue.popleft()

                for dr, dc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]:
                    if (
                        dr >= 0 and dc >= 0 and
                        dr < rows and dc < cols and
                        grid[dr][dc] == "1"
                    ):
                        queue.append((dr, dc))
                        grid[dr][dc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    self.res += 1
        
        return self.res