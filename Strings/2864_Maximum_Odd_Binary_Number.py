class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=s.count('1')
        res=""
        res = '1' * (n-1)
        res = res + '0' * (len(s)-n)
        res = res + '1'
        return res

