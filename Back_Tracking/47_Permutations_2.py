class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            element = nums[i]
            rem = nums[:i] + nums[i+1:]
            for p in self.permuteUnique(rem):
                res.append([element] + p)
        return res
        
