class Solution:
    def findLucky(self, arr: list[int]) -> int:
        f = {}
        for i in arr:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        result = -1
        for i in f:
            if f[i] == i:
                result = max(result, i)
        
        return result
