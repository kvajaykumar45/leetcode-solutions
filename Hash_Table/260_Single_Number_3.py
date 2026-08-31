class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xr = 0
        for each in nums:
            xr = xr ^ each
        a = 0
        b = 0
        diff = xr & -xr
        for each in nums:
            if each & diff == 0:
                a = a ^ each
            else:
                b = b ^ each
        return [a,b]
        
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        k=[]
        for each in nums:
            if each not in d:
                d[each] = 1
            else:
                d[each] += 1
        for each in d:
            if d[each] == 1:
                k.append(each)
        return k
'''
