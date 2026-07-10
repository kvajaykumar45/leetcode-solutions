class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        l1 = s1.split()
        l2 = s2.split()

        for each in l1:
            d[each] = d.get(each,0) + 1
        
        for each in l2:
            d[each] = d.get(each,0) + 1
        ans = []
        for each in d:
            if d[each] == 1:
                ans.append(each)
        return ans
        