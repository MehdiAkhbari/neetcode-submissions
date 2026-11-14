class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u, d, l, r = 0, len(matrix) -1, 0, len(matrix[0]) -1
        i = j = 0
        c = 0
        out = []
        if len(matrix) == 1:
            return matrix[0]

        while True: 
            # shift right       
            while j <= r:
                out.append(matrix[i][j])
                c += 1
                if j < r:
                    j += 1
                else:
                    u += 1
                    i += 1
                    break


            # shift down
            while i <= d:
                out.append(matrix[i][j])
                c += 1
                if i < d:
                    i += 1
                else:
                    r -= 1
                    j -= 1
                    break
            
            
            # shift left
            while j >= l:
                out.append(matrix[i][j])
                c += 1
                if j > l:
                    j -= 1
                else:
                    d -= 1
                    i -= 1
                    break

            while i >= u : 
                out.append(matrix[i][j])
                c += 1
                if i > u:
                    i -= 1
                else:
                    l += 1
                    j += 1
                    break

            if c >= len(matrix) * len(matrix[0]) :
                break

        return(out[0 : len(matrix) * len(matrix[0])])
            