class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        h = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                for k in range(n):
                    if i ==j or j == k or k == i:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 and num not in h:
                        h.add(num)
        return len(h)
        
