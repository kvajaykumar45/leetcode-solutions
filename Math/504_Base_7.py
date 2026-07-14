class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result=""
        if num == 0:
            return "0"
        elif num > 0:
            while num>0:
                result = str(num%7) + result
                num = num//7
            return result
        else:
            num=-num
            while num>0:
                result = str(num%7) + result
                num = num//7
            return '-'+(result)
        

