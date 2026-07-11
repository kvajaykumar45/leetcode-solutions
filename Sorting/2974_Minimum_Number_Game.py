class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        a = []
        nums.sort()
        while len(nums) > 0:
            u = nums.pop(0)  
            v = nums.pop(0) 
            a.extend([v, u])  
        return a
