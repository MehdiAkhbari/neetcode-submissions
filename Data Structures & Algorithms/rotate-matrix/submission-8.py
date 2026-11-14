class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(-int(-n/2)):
            for j in range(-int(-n//2)):
                    temp = matrix[j][-i-1]
                    matrix[j][-i-1] = matrix[i][j]
                    # print(matrix)
                    temp2 = matrix[-i-1][-j-1]
                    matrix[-i-1][-j-1] = temp
                    # print(matrix)
                    temp3 = matrix[-j-1][i]
                    matrix[-j-1][i] = temp2
                    # print(matrix)
                    matrix[i][j] = temp3
                    print(matrix)