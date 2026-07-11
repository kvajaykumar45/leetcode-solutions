class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] <= nums[i-1]:
                break   
            else:
                i += 1
        else:
            return True 
        def isIncreasing(removeIndex):
            prev = None
            for j in range(n):
                if j == removeIndex:
                    continue  # skip removed element
                if prev is not None and nums[j] <= prev:
                    return False
                prev = nums[j]
            return True

        
        return isIncreasing(i-1) or isIncreasing(i)

       
        
