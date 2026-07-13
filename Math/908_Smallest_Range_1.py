class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        big=max(nums) - k
        small=min(nums) + k 
        
        if big<=small:
            return 0
        else:
            return big-small

        
