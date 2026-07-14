class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for each in range(1,num+1):
            sumeach=0
            while each > 0:
                sumeach += each % 10
                each //= 10
            if sumeach % 2 == 0:
                count += 1 
        return count
            


        
