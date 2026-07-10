class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for each in arr:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        h = set()
        for each in d:
            if d[each] in h:
                return False
            else:
                h.add(d[each])
        return True
        
