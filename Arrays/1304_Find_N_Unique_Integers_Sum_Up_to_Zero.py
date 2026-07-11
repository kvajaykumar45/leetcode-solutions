class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        s = 0
        for i in range(1,n):
            res.append(i)
            s = s + i
        res.append(-s)
        return res
        
