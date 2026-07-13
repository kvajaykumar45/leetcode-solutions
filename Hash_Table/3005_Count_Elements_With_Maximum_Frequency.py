class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        maxfreq = max(d.values())
        totalfreq = 0
        for i in d:
            if d[i] == maxfreq:
                totalfreq += d[i]
        return totalfreq

        
