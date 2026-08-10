class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            print('returning')
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        self.res = 0

        def bfs(row, col):
            count = 0
            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                r, c = queue.popleft()
                count += 1
                # print(queue, count, (r, c))

                for dr, dc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]:
                    if (
                        dr >= 0 and dc >= 0 and
                        dr < rows and dc < cols and
                        grid[dr][dc] == 1 and
                        (dr, dc) not in visited
                    ):
                        visited.add((dr, dc))
                        queue.append((dr, dc))
            
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    self.res = max(self.res, bfs(r, c))
        
        return self.res
