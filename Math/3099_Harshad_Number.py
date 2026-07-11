class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        y = x
        while x!=0:
            r = x % 10
            s = s + r
            x = x // 10
        if y % s == 0:
            return s
        else:
            return -1
        
