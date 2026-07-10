class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d = {}
        for each in nums:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        print(d)
        s = 0
        for key in d:
            if d[key]%k == 0:
                s += key * d[key]
        return s
        
