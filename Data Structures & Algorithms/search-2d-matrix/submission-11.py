class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix) - 1
        row_len = len(matrix[0]) - 1

        while a <= b:
            i = (a + b) // 2

            if matrix[i][0] > target:
                b = i - 1
            elif matrix[i][row_len] < target:
                a = i + 1
            else:
                break
				
        a = 0
        b = row_len

        while a <= b:
            j = (a + b) // 2

            if matrix[i][j] > target:
                b = j - 1
            elif matrix[i][j] < target:
                a = j + 1
            else:
                return True

        return False
