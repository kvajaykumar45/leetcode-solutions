class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=[0]*len(nums)
        rightSum=[0]*len(nums)
        i=0
        while i < len(nums):
            leftSum[i]=sum(nums[:i])
            rightSum[i]=sum(nums[(i+1):])
            i+=1
        diff=[0]*len(nums)
        i=0
        while i<len(nums):
            diff[i]=abs(leftSum[i]-rightSum[i])
            i+=1
        return diff

        
