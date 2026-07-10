class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        '''
        maxindex = 0
        maxsum = sum(grid[0])
        i = 1
        while i < len(grid):
            x = sum(grid[i])
            if x > maxsum:
                maxindex = i
                maxsum = x 
            i += 1
        return maxindex
        '''

        ans = 0
        best = 0
        for i in range(len(grid)):
            s = sum(grid[i])
            if s > best:
                ans = i
                best = s
        return ans
        
        
