class Solution:
    def tribonacci(self, n: int) -> int:
        t0=0
        t1=1
        t2=1
        if n == 1:
            return t1
        if n == 2:
            return t2
        
        count = 3
        t3=0
        while count <= n:
            t3 = t0 + t1 + t2
            count += 1
            t0 = t1
            t1 = t2
            t2 = t3

        return t3 
        

        
