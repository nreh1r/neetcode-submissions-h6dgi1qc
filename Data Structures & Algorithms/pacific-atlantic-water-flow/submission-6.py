class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        res = []

        def bfs(source, grid):
            queue = deque(source)

            while queue:
                r, c = queue.popleft()
                grid[r][c] = True

                for dr, dc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]:
                    if (
                        0 <= dr < rows and
                        0 <= dc < cols and
                        heights[dr][dc] >= heights[r][c] and
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
                    res.append([r, c])
        
        return res