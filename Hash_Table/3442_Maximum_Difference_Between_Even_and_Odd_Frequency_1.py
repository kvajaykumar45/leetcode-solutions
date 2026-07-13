class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        oddmax = 0
        evenmin = 100
        for i in d:
            if d[i] % 2 !=0:
                if d[i] > oddmax:
                    oddmax = d[i]
            else:
                if d[i] < evenmin:
                    evenmin = d[i]
        return oddmax - evenmin
        
