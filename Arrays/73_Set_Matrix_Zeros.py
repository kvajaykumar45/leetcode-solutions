class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * m 
        col = [0] * n

        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        print(row)
        print(col)
        
        for each in range(m):
            if row[each] == 1:
                for i in range(n):
                    matrix[each][i] = 0
        
        for each in range(n):
            if col[each] == 1:
                for i in range(m):
                    matrix[i][each] = 0

        

        
        
