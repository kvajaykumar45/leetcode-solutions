class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        total = len(nums)
        pos=0
        neg=0
        for i in range(0,total):
            if nums[i] < 0:
                neg += 1
            elif nums[i] > 0:
                pos += 1
        return pos if pos > neg else neg


        
