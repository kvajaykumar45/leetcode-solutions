class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        minimum = 201
        for each in tasks:
            x = each[0] + each[1]
            if x < minimum:
                minimum = x
        return minimum

        
