class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range(1,len(rings),2):
            if rings[i] not in d:
                d[rings[i]] = list(rings[i-1])
            else:
                d[rings[i]].append(rings[i-1])
        count = 0
        for i in d.values():
            if len(set(i)) == 3:
                count+=1
        return count
        
