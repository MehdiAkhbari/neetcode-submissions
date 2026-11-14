# watch the solution video for the smart idea using hash maps in place of the matrix
# it's not straightforward if you haven't seen tis question before. 
# First idea: use a hash map for each row and column which determines if that row or column should be zeroed (thos will be O(m+n) memory)
# Second idea: instead of using an external hash map, use first row and column of the matrix (plus one additional number rowZero) as the hash map. If they are zero means that their corresponding row or column shoud be zeored.
# Note that first row and first column should not be zeored before zeroing other elements because they affect whether other elements are zeroed.
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

                    
        