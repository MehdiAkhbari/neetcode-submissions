# My idea: rotate 4 points at each repeat (i, j)->(-j, i)->(-i, -j)->(-j, i)->(i, j) 
# Note: -i and -j here mean n-1-i and n-1-j in python
# Also, you noly should rotate the first quadrant of the matrix i.e (i, j) <= ceil(n) (check it graphically)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(-int(-n/2)):
            for j in range(-int(-n//2)):
                    temp = matrix[j][n-1-i]
                    matrix[j][n-1-i] = matrix[i][j]
                    temp2 = matrix[n-1-i][n-1-j]
                    matrix[n-1-i][n-1-j] = temp
                    temp3 = matrix[n-1-j][i]
                    matrix[n-1-j][i] = temp2
                    matrix[i][j] = temp3
                    print(matrix)