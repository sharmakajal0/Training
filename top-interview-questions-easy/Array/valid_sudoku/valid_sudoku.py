from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])

        for i in range(len(board)):
            res1 = self.valid_row(i, board)
            res2 = self.valid_column(i, board)

            if (res1 < 1 or res2 < 1):
                return False
        
        res3 = self.valid_subsquares(board)
        if (res3 < 1):
            return False
        return True
    
    def valid_row(self, row, board):
        temp_row = board[row]
        temp = []
        for a in range(len(temp_row)):
            if temp_row[a] != 0:
                temp.append(temp_row[a])
        if any(i < 0 and i > 9 for i in temp):
            return -1
        elif len(temp) != len(set(temp)):
            return 0
        else:
            return 1

    def valid_column(self, col, board):
        temp_col = []
        for row in board:
            temp_col.append(row[col])
        temp = []
        for a in range(len(temp_col)):
            if temp_col[a] != 0:
                temp.append(temp_col[a])
        if any(i < 0 and i > 9 for i in temp):
            return -1
        elif len(temp) != len(set(temp)):
            return 0
        else:
            return 1

    def valid_subsquares(self, board):
        for row in range(0, 9, 3):
            for col in range(0,9,3):
                temp = []
                for r in range(row,row+3):
                    for c in range(col, col+3):
                        if board[r][c] != 0:
                            temp.append(board[r][c])
                if any(i < 0 and i > 9 for i in temp):
                    return -1
                elif len(temp) != len(set(temp)):
                    return 0
        return 1

board = [
         ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
]

is_valid_sudoku = Solution()
print(is_valid_sudoku.isValidSudoku(board))

board = [
    ["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
is_valid_sudoku = Solution()
print(is_valid_sudoku.isValidSudoku(board))