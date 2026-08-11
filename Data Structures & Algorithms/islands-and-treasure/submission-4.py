class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2 ** 31 - 1
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            row, col = queue.popleft()

            for dr, dc in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]:
                if (
                    dr >= 0 and dc >= 0 and
                    dr < rows and dc < cols and
                    grid[dr][dc] == INF
                ):
                    grid[dr][dc] = grid[row][col] + 1
                    queue.append((dr, dc))