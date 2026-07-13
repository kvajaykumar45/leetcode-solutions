class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        cols = len(grid[0])
        result = []

        for j in range(cols):
            max_width = max(len(str(grid[i][j])) for i in range(len(grid)))
            result.append(max_width)

        return result
