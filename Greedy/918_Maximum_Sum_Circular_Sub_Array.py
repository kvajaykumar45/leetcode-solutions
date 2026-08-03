class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalsum = sum(nums)

        currsum = nums[0]
        maxsum = nums[0]
        i = 1
        while i < len(nums):
            if currsum < 0:
                currsum = 0
            currsum += nums[i]
            maxsum = max(currsum, maxsum)
            i += 1
        
        minsum = nums[0]
        currsum = nums[0]
        i = 1
        while i < len(nums):
            currsum += nums[i]
            currsum = min(nums[i], currsum)
            minsum = min(minsum, currsum)
            i += 1
        
        if maxsum < 0 :
            return maxsum

        return max(maxsum, totalsum - minsum)
        
        
