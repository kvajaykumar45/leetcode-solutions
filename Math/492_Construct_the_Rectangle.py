import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(math.sqrt(area))
        while W > 0:
            if area % W == 0:
                L = area // W
                return [L, W] 
            W -= 1
