class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while True:
            nums = self.round(nums)
            if len(nums) == 1:
                return nums[0]

    def round(self, nums):
        n = len(nums)
        newNums = [0] * (n//2)
        i = 0 
        while i < len(newNums):
            if i % 2 == 0:
                newNums[i] = min(nums[2*i], nums[2*i+1])
            else:
                newNums[i] = max(nums[2*i], nums[2*i+1])
            i = i + 1
        return newNums


        
