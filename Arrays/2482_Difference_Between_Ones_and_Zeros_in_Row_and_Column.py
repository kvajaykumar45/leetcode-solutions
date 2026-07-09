class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesrow = []
        onescol = []
        zerosrow = []
        zeroscol = []
        for row in grid:
            zerocount = onecount = 0
            for element in row:
                if element == 0:
                    zerocount += 1
                else:
                    onecount += 1
            onesrow.append(onecount)
            zerosrow.append(zerocount)
        rows = len(grid)
        cols = len(grid[0])
        i = 0
        for i in range(cols):
            zerocount = onecount = 0
            for j in range(rows):
                if grid[j][i] == 0:
                    zerocount += 1
                else:
                    onecount += 1
            onescol.append(onecount)
            zeroscol.append(zerocount)
        diff = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = onesrow[i]+onescol[j]-zerosrow[i]-zeroscol[j]
                row.append(element)
            diff.append(row)
        return diff



        return grid

                


        