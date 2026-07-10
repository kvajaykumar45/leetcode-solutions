class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        m = n
        while n > 0:
            r = n % 10
            s += r
            p *= r
            n = n // 10
        #print(s+p)
        return m % (s+p) == 0
            

        
