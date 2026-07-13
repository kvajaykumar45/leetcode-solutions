class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length=1
        maxlength=1
        for i in range(0, len(nums)-1):
            if nums[i+1] > nums[i]:
                length += 1
            else:
                if length > maxlength:
                    maxlength = length
                length=1
        else:
            if length > maxlength:
                maxlength = length
        return maxlength





        
