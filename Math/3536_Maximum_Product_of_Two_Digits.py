class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n!=0:
            r = n%10
            digits.append(r)
            n = n // 10
        maxp = 0
        p = 0
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i != j:
                    p = digits[i] * digits[j]
                    if p > maxp:
                        maxp=p
        return maxp

        
