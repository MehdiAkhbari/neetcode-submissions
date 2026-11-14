class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # num of rows
        n = len(matrix[0]) # num of cols

        l = 0
        u = 0
        r = n - 1 
        d = m - 1
        print(matrix[d][r])

        # find row:
        while True:
            # print(u, d)
            if target < matrix[u][0] or target > matrix[d][-1]:
                return False
            elif target >= matrix[u][0] and target <= matrix[u][-1]:
                row = u
                break 
            elif target >= matrix[d][0] and target <= matrix[d][-1]:
                row = d
                break 
            elif d - u <= 1:
                return False
            else:
                mid_row = (u + d) // 2
                if target > matrix[mid_row][-1]:
                    u = mid_row + 1
                elif target < matrix[mid_row][0]:
                    d = mid_row - 1
                elif target <= matrix[mid_row][-1] and target >= matrix[mid_row][0]:
                    row = mid_row
                    break
        print(row)
        # find column:


        while True:

            if target == matrix[row][l] or target == matrix[row][r]:
                return True
            elif r - l <= 1:
                return False 
            else:
                mid_col = (l + r) // 2
                if target >= matrix[row][mid_col]:
                    l = mid_col
                elif target < matrix[row][mid_col]:
                    r = mid_col

            



                    


                    
