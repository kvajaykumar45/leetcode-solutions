class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        c = len(citations)
        for i in range(0,c):
            if  citations[i] < (i+1):
                return i
        return c

        
