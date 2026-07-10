class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])         # sum of first k elements
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # slide the window
            max_sum = max(max_sum, window_sum)

        return max_sum / k
