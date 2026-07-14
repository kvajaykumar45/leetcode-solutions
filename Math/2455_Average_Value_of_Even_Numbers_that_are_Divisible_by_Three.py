class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum1=0
        count1=0
        for each in nums:
            if each%6==0:
                count1=count1+1
                sum1=sum1+each
        if count1==0:
            return 0
        return sum1//count1



        
