class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(1, n, 2):
            s = s + nums[i-1] - nums[i] 
        if n%2 == 1:
            s = s + nums[-1]
        return s
