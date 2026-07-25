class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        misses = 0
        mismatch = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                misses += 1
                mismatch.append(i)
                if misses > 2:
                    return False 
        print(mismatch)
        if misses == 2:
            i,j = mismatch
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False
        else:
            return False
