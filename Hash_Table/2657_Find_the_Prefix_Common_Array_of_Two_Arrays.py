class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        d = {}
        c = []
        count = 0       
        for i,j in zip(A,B):
            d[i] = d.get(i,0) + 1
            if d[i] == 2:
                count = count + 1

            d[j] = d.get(j,0) + 1
            if d[j] == 2:
                count = count + 1
            
            c.append(count)

        return c