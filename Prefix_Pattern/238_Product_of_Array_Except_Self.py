class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = 1
        suffix[-1] = 1
        p = 1
        for i in range(1, n):
            p = p * nums[i-1]
            prefix[i] = p
        p = 1
        for i in range(n-1, 0, -1):
            p = p * nums[i]        
            suffix[i-1] = p
        result = []
        for i in range(n):
            result.append(prefix[i]*suffix[i])
        return result
    