class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            quotient = columnNumber % 26
            result = chr(quotient + 65) + result
            columnNumber = columnNumber // 26 

        return result
