class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == ".":
                    continue
                
                if (
                    col in rows[i] or
                    col in cols[j] or
                    col in squares[str(i // 3) + str(j // 3)]
                ):
                    return False

                rows[i].add(col)
                cols[j].add(col)
                squares[str(i // 3) + str(j // 3)].add(col)
        return True

