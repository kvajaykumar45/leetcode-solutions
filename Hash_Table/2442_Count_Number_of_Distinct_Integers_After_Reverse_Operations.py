class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set(nums)
        for num in nums:
            rev = 0
            while num > 0:
                # r = num % 10
                rev = rev * 10 + num % 10
                num = num // 10
            d.add(rev)
        return len(d)
        
        
            

    
    
        
