class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        cvalue=0
        if left == right:
            return nums[left]
        while left<right:
            #number=int(str(nums[left]) + str(nums[right]))
            a=nums[left]
            b=nums[right]
            digits=0
            while b>0:
                b=b//10
                digits+=1
                
            number = (nums[left] * (10**digits)) + nums[right]
            print(number)
            cvalue += number
            left+=1
            right-=1
        if left == right:
            cvalue+=nums[left]
        return cvalue
