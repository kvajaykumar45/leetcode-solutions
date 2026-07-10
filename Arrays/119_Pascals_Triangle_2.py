class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        n=rowIndex
        for k in range(1,n+1): 
            x = row[-1] * (n-k+1)//k
            row.append(x)
        return row
