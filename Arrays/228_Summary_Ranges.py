class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return [] 
        result = []
        i=1
        start=nums[0]
        while i < len(nums):
            if (nums[i] - nums[i-1]) != 1:
                if start == nums[i-1]:
                    result.append(str(start))
                else:           
                    result.append(str(start)+"->"+str(nums[i-1]))
                start=nums[i]
            i += 1
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start)+"->"+str(nums[-1]))
        
        return result

            


        
