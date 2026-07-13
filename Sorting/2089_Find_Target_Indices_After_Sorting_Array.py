class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targets=[]
        nums.sort()
        for  i in range(0,len(nums)):
            if nums[i] == target:
                targets.append(i)
        return targets

        
