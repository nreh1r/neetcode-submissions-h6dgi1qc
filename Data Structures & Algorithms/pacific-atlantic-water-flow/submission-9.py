class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        result = []

        def bfs(source, grid):
            queue = deque(source)

            while queue:
                row, col = queue.popleft()
                grid[row][col] = True

                for dr, dc in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1)
                ]:
                    if (
                        0 <= dr < rows and
                        0 <= dc < cols and
                        heights[dr][dc] >= heights[row][col] and
                        not grid[dr][dc]
                    ):
                        queue.append((dr, dc))

        pacific = []
        atlantic = []

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    result.append([r, c])
        
        return result