class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k1 = len(s)
        k2 = len(t)
        i = 0
        j = 0
        c = 0
        while i<k1 and j<k2:
            if s[i] == t[j]:
                i += 1
                j += 1
                c += 1
            else:
                j += 1
        return k1 == c


        
