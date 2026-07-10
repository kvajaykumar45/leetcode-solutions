class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums) - nums[0]
        if leftsum == rightsum:
            return 0

        for i in range(1, len(nums)):
            leftsum = leftsum + nums[i-1]
            rightsum = rightsum - nums[i]
            #print(leftsum, rightsum)
            if leftsum == rightsum:
                return i
        else:
            return -1
        
