class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        leftsum=0
        totalsum=sum(nums)
        for i in range(0,len(nums)):
            #rightsum=totalsum - nums[i] - leftsum
            if leftsum == totalsum - nums[i] - leftsum:
                return i
            leftsum += nums[i]
        return -1

