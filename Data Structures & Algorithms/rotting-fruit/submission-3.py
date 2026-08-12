class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        num_fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_fresh += 1
                
                if grid[r][c] == 2:
                    queue.append((r, c))

        if num_fresh == 0:
            return 0
        
        curr_rotten = 0
        num_minutes = 0
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
                    grid[dr][dc] == 1
                ):
                    grid[dr][dc] = grid[row][col] + 1
                    queue.append((dr, dc))
                    curr_rotten += 1
                    num_minutes = max(num_minutes, grid[dr][dc])

            if curr_rotten == num_fresh:
                return num_minutes - 2
            

        return -1
            