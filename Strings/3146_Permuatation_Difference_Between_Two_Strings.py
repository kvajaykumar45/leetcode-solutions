class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index1 = 0
        result = 0
        while index1 < len(s):
            index2 = t.index(s[index1])
            result += abs(index1 - index2)
            index1 += 1
        return result
        
