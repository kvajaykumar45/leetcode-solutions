class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = [0] * n
        mini = [0] * n
        
        maxi[0] = nums[0]
        for i in range(1,n):
            maxi[i] = max(nums[i], maxi[i-1])
        
        mini[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            mini[i] = min(nums[i], mini[i+1])
        
        for i in range(n):
            if (maxi[i] - mini[i]) <= k:
                return i
        
        return -1
