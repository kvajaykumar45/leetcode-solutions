class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        while left < right:
            while nums[left] % 2 == 0 and left < right:
                left += 1
            while nums[right] % 2 == 1 and left < right:
                right -= 1
            nums[left],nums[right] = nums[right],nums[left]
        return nums
        
