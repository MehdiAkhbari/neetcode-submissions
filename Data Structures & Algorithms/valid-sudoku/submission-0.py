class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_hash = [[0 for _ in range(9)] for _ in range(9)] 
        cols_hash = [[0 for _ in range(9)] for _ in range(9)] 
        sqs_hash = [[0 for _ in range(9)] for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j]) - 1
                    # print(val)
                    rows_hash[i][val] += 1 
                    cols_hash[j][val] += 1
                    # print(cols_hash[j][val - 1] )
                    sq_num = (i // 3) * 3 + j // 3                      
                    sqs_hash[sq_num][val] += 1

                    if (rows_hash[i][val] > 1 or cols_hash[j][val] > 1 or sqs_hash[sq_num][val] > 1):
                        return False
        print(sqs_hash)
        return True

 