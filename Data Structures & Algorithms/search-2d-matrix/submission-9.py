class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            row_mid = (top + bot) // 2

            if matrix[row_mid][0] > target:
                bot = row_mid - 1
            elif matrix[row_mid][-1] < target:
                top = row_mid + 1
            else:
                break
        
        if not (top <= bot):
            return False
        row_mid = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row_mid][mid] < target:
                l = mid + 1
            elif matrix[row_mid][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False



