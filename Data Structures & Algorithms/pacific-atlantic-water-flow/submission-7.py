class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        pacific, atlantic = set(), set()
        res = []

        def dfs(row, col, visited, grid, prevHeight):
            if (
                row < 0 or row == rows or
                col < 0 or col == cols or
                heights[row][col] < prevHeight or
                (row, col) in visited
            ):
                return
            
            visited.add((row, col))
            grid[row][col] = True
            dfs(row + 1, col, visited, grid, heights[row][col])
            dfs(row - 1, col, visited, grid, heights[row][col])
            dfs(row, col + 1, visited, grid, heights[row][col])
            dfs(row, col - 1, visited, grid, heights[row][col])
        

        for c in range(cols):
            dfs(0, c, pacific, pac, heights[0][c])
            dfs(rows - 1, c, atlantic, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, pac, heights[r][0])
            dfs(r, cols - 1, atlantic, atl, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        
        return res