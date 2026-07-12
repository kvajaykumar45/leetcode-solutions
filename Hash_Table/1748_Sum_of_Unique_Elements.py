class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        f = {}
        for each in nums:
            if each not in f:
                f[each] = 1
            else:
                f[each] += 1
        #print(f)
        s=0
        for each in f:
            #print(f[each])
            if f[each] == 1:
                s += each
        return s
