class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minrow = []
        maxcol = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            minrow.append(min(matrix[i]))
        

        for i in range(n):
            maxi = 0
            for j in range(m):
                if matrix[j][i] > maxi:
                    maxi = matrix[j][i]
            maxcol.append(maxi)
    
        #print(minrow)
        #print(maxcol)

        result = []
        for i in minrow:
            if i in maxcol:
                result.append(i)
        return result



        
