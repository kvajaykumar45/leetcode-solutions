class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum([ x for x in range(max(1,n-k), n+k+1) if ((n & x) == 0)])