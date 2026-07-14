import math
class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return False
        sq = int(math.sqrt(n))
        if sq * sq != n:
            return False
        
        count = 0
        for i in range(2, sq//2+1):
            if sq % i == 0:
                count = count + 1
                break
        if count == 0:
            return True
        else:
            return False
                

        
