class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                possible = nums[i-1] + 1
                moves += possible - nums[i]
                nums[i] = possible
        return moves
        
