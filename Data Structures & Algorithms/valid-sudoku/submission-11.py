class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num == ".":
                    continue
                    
                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)
                
                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)
                
                if num in squares[tuple([row // 3, col // 3])]:
                    return False
                else:
                    squares[tuple([row // 3, col // 3])].add(num)
        
        return True

