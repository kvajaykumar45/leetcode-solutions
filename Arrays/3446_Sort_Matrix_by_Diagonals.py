from collections import defaultdict
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                diagonals[i-j].append(grid[i][j])
        for k in diagonals:
            if k >= 0:
                diagonals[k].sort()
            else:
                diagonals[k].sort(reverse=True)
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = diagonals[i-j].pop()
        return grid
        
        