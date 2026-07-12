class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxdiff = 0
        i = 0
        while i < len(nums) - 1:
            diff = nums[i+1] - nums[i]
            if diff > maxdiff:
                maxdiff = diff
            i += 1
        return maxdiff
