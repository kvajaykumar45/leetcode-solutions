class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for k in range(n):
            i = 0
            j = n-1
            while i <= j:
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
                i += 1
                j -= 1
        
        
