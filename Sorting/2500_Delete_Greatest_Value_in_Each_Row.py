class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total=0
        for row in grid:
            row.sort()
        for col in zip(*grid):
            total += max(col)
                       
        return total


        
