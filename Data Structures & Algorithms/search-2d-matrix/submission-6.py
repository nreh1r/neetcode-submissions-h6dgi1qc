class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Need to calculate row_mid and col_mid to get the middle of the matrix
        row_t, row_b = 0, len(matrix) - 1

        # Have row jumping as the outer loop
        while row_t <= row_b:
            row_mid = (row_t + row_b) // 2
            # Now do regular binary search on the row

            col_l, col_r = 0, len(matrix[0]) - 1
            while col_l <= col_r:
                print(f"col_l: {col_l}; col_r: {col_r}, row_mid: {row_mid}")
                col_mid = (col_l + col_r) // 2

                if matrix[row_mid][col_mid] < target:
                    col_l = col_mid + 1
                elif matrix[row_mid][col_mid] > target:
                    print("updating col_r")
                    col_r = col_mid - 1
                else:
                    return True
            
            # See which way we need to update the rows
            print(col_r)
            if col_r < (len(matrix[0]) - 1) // 2:
                row_b = row_mid - 1
            else:
                row_t = row_mid + 1
        
        return False


