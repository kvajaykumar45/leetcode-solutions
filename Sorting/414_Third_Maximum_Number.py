class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = list(set(nums))
        if len(n) < 2:
            return n[0]
        if len(n) < 3:
            if n[0] > n[1]:
                return n[0]
            else:
                return n[1]
        
        return sorted(n)[-3]


        
