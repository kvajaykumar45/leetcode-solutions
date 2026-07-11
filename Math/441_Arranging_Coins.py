class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        dollars = 1
        while dollars <= n:
            i += 1
            dollars += i
        return i - 1
        
