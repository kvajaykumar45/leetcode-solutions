class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a = n * n #oddsum
        b = n * (n + 1) #evensum

        while b!=0:
            r = a % b
            a = b
            b = r
        return a


        
"""
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

"""
