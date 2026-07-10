class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        #print(d)
        pairs = 0
        leftover = 0
        for each in d:
            if d[each] % 2 == 0:
                pairs += d[each] // 2
            else:
                pairs += d[each] // 2
                leftover += d[each] % 2
        
        return [pairs, leftover]
