class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()
        self.res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_fresh += 1
                
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while num_fresh and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1)
                ]:
                    if (
                        0 <= dr < rows and
                        0 <= dc < cols and
                        grid[dr][dc] == 1
                    ):
                        grid[dr][dc] = 2
                        num_fresh -= 1
                        queue.append((dr, dc))
            self.res += 1
        
        return self.res if num_fresh == 0 else -1
