class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n!=1:
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1])%10
            n = n-1
        return nums[0]

"""
from math import comb

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans += nums[i] * comb(n - 1, i)
        return ans % 10
"""S
