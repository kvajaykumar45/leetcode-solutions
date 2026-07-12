class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for each in grid:
            for k in each:
                if k<0:
                    count += 1
        return count
        
