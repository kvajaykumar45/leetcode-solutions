class Solution:
    def isHappy(self, n: int) -> bool:
        seq = set()
        
        sqsum=0
        while True:
            while n != 0:
                r = n % 10
                sqsum = sqsum + r*r
                n = n // 10
        
            if sqsum == 1:
                return True
            elif sqsum in seq:
                return False
            else:
                seq.add(sqsum)
                n=sqsum
                sqsum=0
        
        
        


        
