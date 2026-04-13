class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue

                # check if the value violates row, column, or square conditions
                if (
                    c in rows[i] or
                    c in cols[j] or
                    c in squares[str(i // 3) + str(j // 3)]
                ):
                    return False
                else:
                    rows[i].add(c)
                    cols[j].add(c)
                    squares[str(i // 3) + str(j // 3)].add(c)
        return True
