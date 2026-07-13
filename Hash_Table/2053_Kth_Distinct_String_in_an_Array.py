
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        distinct = 0
        for i in d:
            if d[i] == 1:
                distinct += 1
                if distinct == k:
                    return i
        else:
            return ""

        
