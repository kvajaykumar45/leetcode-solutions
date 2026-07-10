class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = num[0]
        for i in range(1,len(num)):
            n = n*10 + num[i]
        n = n + k
        res = []
        while n > 0:
            r = n % 10
            res.append(r)
            n = n // 10
        return res[::-1]

        
