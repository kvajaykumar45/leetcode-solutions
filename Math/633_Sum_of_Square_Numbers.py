class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = math.floor(math.sqrt(c))
        while a<=b:
            s = a**2 + b**2
            if s == c:
                return True
            elif s > c:
                b -= 1
            elif s < c:
                a += 1
        return False
