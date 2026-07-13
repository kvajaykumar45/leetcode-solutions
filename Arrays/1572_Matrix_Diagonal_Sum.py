class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        i = 0
        diagonalsum = 0
        while i < rows:
            diagonalsum += mat[i][i]
            i += 1
        i=0
        j=rows-1
        while i < rows:
            if i != j:
                diagonalsum += mat[i][j]
            i += 1
            j -= 1
        return diagonalsum
    
        

        
