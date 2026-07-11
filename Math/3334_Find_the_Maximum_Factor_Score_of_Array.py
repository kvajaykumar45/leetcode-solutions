import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        def factor_score(arr):
            g = arr[0]
            l = arr[0]
            for x in arr[1:]:
                g = math.gcd(g, x)
                l = l * x // math.gcd(l, x)
            return g * l

        if n == 1:
            return nums[0] * nums[0]

        max_score = factor_score(nums)  
        #max_score = 0

        for i in range(n):
            new_nums = nums[:i] + nums[i+1:]
            max_score = max(max_score, factor_score(new_nums))

        return max_score
