class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        self.res = []

        def bfs(row, col):
            queue = deque([(row, col)])
            visited = set()
            visited.add((row, col))
            pacific = False
            atlantic = False

            while queue:
                r, c = queue.popleft()

                if r == 0 or c == 0:
                    pacific = True
                
                if r == rows - 1 or c == cols - 1:
                    atlantic = True
                
                for dr, dc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]:
                    if (
                        dr >= 0 and dc >= 0 and
                        dr < rows and dc < cols and
                        heights[dr][dc] <= heights[r][c]
                        and (dr, dc) not in visited
                    ):
                        queue.append((dr, dc))
                        visited.add((dr, dc))
            
            return pacific and atlantic

        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    self.res.append([r, c])

        return self.res