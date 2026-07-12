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
        
