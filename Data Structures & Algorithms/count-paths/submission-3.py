class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [0] * m
        mat = [ans] * n 
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i-1][j] + mat[i] [j-1]

        return mat[n-1][m-1]