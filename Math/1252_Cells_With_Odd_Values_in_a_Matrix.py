class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        nums =  [ [0]*n for i in range(m)]
        for x,y in indices:
            for k in range(n):
                nums[x][k] += 1
            for k in range(m):
                nums[k][y] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if nums[i][j] & 1:
                    count += 1
        return count
        
