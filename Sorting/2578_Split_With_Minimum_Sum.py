class Solution:
    def splitNum(self, num: int) -> int:
        nums=[]
        while num>0:
            r=num%10
            nums.append(r)
            num//=10
        nums.sort()
        new1=nums[0]
        new2=nums[1]
        for i in range(2,len(nums),2):
            new1=new1*10+nums[i]
            if (i+1)<len(nums): 
                new2=new2*10+nums[i+1]
        return new1+new2


        
