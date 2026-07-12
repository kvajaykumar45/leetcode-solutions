class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        return nums[-2]
        
"""
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        mini = min(nums)
        maxi = max(nums)
        for x in nums:
            if x != mini and x!= maxi:
                return x
"""
