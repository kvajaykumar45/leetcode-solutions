class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        print(d)
        odd = False
        total = 0
        for each in d.values():
            if each % 2 == 1 and not odd:
                odd = True
                total += each
            elif each % 2 == 1:
                total += each - 1
            else:
                total += each
        return total
