#!/usr/bin/python3

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero, first_col_has_zero = False, False
        
        for i in range(n):
            if matrix[0][i] == 0:
                first_row_has_zero = True
        
        for j in range(m):
            if matrix[j][0] == 0:
                first_col_has_zero = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0



obj = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj.setZeroes(matrix)
print(matrix) 