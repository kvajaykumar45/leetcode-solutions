class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
       
        intervals.sort(key = lambda x:x[1])
        prevend = intervals[0][1]
        removed = 0
        for i in range(1, len(intervals)):
            currentstart = intervals[i][0]
            if currentstart >= prevend:
                prevend = intervals[i][1]
            else:
                removed += 1
        return removed
        
