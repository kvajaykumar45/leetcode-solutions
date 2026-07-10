class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result =list(list())
        for i in range(1, n-1):
            row = []
            for j in range(1, n-1):
                m = 1
                for p in range(i-1, i+2):
                    for q in range(j-1, j+2):
                        if grid[p][q] > m:
                            m = grid[p][q]
                row.append(m)
            result.append(row)
        return result
                



        
