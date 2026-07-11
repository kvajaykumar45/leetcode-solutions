class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for h in range(4):
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
            for k in range(n):
                i = 0
                j = n-1
                while i <= j:
                    mat[k][i], mat[k][j] = mat[k][j], mat[k][i]
                    i += 1
                    j -= 1
            if mat == target:
                return True
        return False

        
        
        
