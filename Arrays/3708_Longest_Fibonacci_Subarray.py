class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        first = nums[0]
        second = nums[1]
        i = 2
        count = 2
        maxseq = 0
        while i < len(nums):
            if nums[i-1] + nums[i-2] == nums[i]:
                count += 1
            else:
                if count > maxseq:
                    maxseq = count
                count = 2
            i += 1
        if i == len(nums):
            if count > maxseq:
                maxseq = count
        return maxseq
