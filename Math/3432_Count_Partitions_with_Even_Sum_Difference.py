class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        lsum=0
        rsum=sum(nums)
        for i in range(0,len(nums)-1):
            lsum += nums[i]
            rsum -= nums[i]
            if abs(lsum - rsum) % 2 == 0:
                count += 1
        return count

        
