class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minIndex=0
            minimum = nums[0]
            for j in range(1,len(nums)):
                if nums[j] < minimum:
                    minIndex = j 
                    minimum = nums[j]
           # print("mini",minimum)
            nums[minIndex] = multiplier * nums[minIndex]
        return nums
                
        
