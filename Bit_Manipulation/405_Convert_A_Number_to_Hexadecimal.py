class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num &= 0xFFFFFFFF
        hex_chars = "0123456789abcdef"
        result = ""
        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16
        return result
        
