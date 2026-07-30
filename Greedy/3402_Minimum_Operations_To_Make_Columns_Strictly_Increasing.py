class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        moves = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(cols):
            for j in range(1, rows):
                if grid[j][i] <= grid[j-1][i]:
                    moves += grid[j-1][i] + 1 - grid[j][i]
                    grid[j][i] = grid[j-1][i] + 1
        return moves

        
