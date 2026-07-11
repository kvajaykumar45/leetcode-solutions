class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x1 = abs(x-z)
        y1 = abs(y-z)
        if x1 > y1:
            return 2
        elif x1 < y1:
            return 1
        else:
            return 0
        
