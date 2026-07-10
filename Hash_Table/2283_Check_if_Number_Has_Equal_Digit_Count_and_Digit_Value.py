class Solution:
    def digitCount(self, num: str) -> bool:

        d = {}
        for i in range(len(num)):
            d[i] = num.count(str(i))
        
        for i in range(len(num)):
            if d[i] != int(num[i]):
                return False
        return True
