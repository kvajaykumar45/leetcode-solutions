class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = self.digitsum(nums[0])
        for each in range(1, len(nums)):
            x = self.digitsum(nums[each])
            m = min(m, x)
        return m
    
    def digitsum(self, n):
        s=0
        while(n!=0):
            s = s + n % 10
            n = n//10
        return s


    
        
