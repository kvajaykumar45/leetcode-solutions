class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1:
            return 1
        a=0
        b=1
        for i in range(2,n+1):
            a, b = b, a+b
        return b
