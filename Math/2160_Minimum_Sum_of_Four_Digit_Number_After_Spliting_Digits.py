class Solution:
    def minimumSum(self, num: int) -> int:
        nums=[]
        while num>0:
            r=num%10
            nums.append(r)
            num//=10
        nums.sort()
        print(nums)
        new1=nums[0]*10+nums[2]
        new2=nums[1]*10+nums[3]
        return new1+new2
        
