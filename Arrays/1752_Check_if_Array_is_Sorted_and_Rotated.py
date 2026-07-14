class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks = 0
        for i in range(0,len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                breaks += 1
            if breaks > 1:
                return False
        return True
