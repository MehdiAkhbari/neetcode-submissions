# watch the solution video for the smart idea using hash maps in place of the matrix

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            if matrix[0][0] == 0:
                matrix[i][0] = 0

        for j in range(len(matrix[0])):
            if rowZero == 0:
                matrix[0][j] = 0

                    
        