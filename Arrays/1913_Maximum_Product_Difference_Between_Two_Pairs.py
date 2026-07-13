class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min2=min1=10000
        max1=max2=0

        for i in nums:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
            
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        #print(max1,max2, min1,min2)
        return max1 * max2 - min1 * min2
