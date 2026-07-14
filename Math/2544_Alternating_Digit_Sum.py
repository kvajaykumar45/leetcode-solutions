class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        result = 0
        for i in str(n):
            if count % 2 != 0:
                result += int(i)
            else:
                result -= int(i)
            count += 1
        return result



        
