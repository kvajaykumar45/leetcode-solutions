class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result=[]
        xi=0
        for each in nums:
            xi=((xi<<1)|each)%5
            result.append(xi==0)
        return result
        
