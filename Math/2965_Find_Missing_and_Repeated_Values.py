class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        actualsum=0
        actualsumsquare=0
        n=0
        for row in grid:
            for col in row:
                actualsum+=col
                actualsumsquare+=(col*col)
                n+=1
        expectedsum=n*(n+1)//2
        expectedsumsquare=n*(n+1)*(2*n+1)//6
        yminusx = expectedsum-actualsum
        y2minusx2=expectedsumsquare-actualsumsquare
        yplusx=y2minusx2//yminusx
        y=(yplusx + yminusx)//2
        x=yplusx-y
        return [x,y]
        
        
        
    


        
