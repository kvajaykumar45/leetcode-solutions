class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i] % 2 !=0:
                x = x+1
            else:
                y = y+1
        return y*[0]+x*[1]
