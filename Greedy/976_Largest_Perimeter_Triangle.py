class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxlength = 0
        for i in range(len(nums)-2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
           
            if (a+b>c) and (b+c>a) and (c+a>b) :
                length = a+b+c
                maxlength = max(length, maxlength)
        return maxlength
