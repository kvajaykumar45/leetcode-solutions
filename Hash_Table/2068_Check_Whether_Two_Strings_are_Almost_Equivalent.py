class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in word1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in word2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        k1 = set(d1.keys()).union(set(d2.keys()))
        
        for i in k1:
            flag = True
            if i in d1 and i in d2:
                diff = abs(d1[i] - d2[i])
            elif i in d1:
                diff = d1[i]
            elif i in d2:
                diff = d2[i]
            if diff > 3:
                flag = False
                break
        return flag
