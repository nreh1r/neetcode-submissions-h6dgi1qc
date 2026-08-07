class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        self.board = [["."] * n for i in range(n)]
        self.res = []

        def dfs(row):
            if row == n:
                self.res.append(["".join(row) for row in self.board])
                return
            
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                self.board[row][col] = "Q"

                dfs(row + 1)

                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                self.board[row][col] = "."
        
        dfs(0)

        return self.res