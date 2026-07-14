class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        b=nums[0]
        for i in nums:
            if i<a:
                a=i
            if i>b:
                b=i
        while b!=0:
            a,b=b,a%b
        return a        
        
