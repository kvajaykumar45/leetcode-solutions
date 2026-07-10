class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for n in range(lowLimit, highLimit+1):
            s = 0
            while n > 0:
                s = s + (n%10)
                n = n // 10
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        #print(d)
        return max(d.values())
                

        
