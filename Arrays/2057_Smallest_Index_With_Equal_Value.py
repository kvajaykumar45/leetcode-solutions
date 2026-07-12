class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i % 10 == nums[i]:
                return i
        else:
            return -1
                
