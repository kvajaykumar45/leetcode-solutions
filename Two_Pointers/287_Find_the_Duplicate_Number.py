"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dups = [0] * len(nums)
        for i in nums:
            if dups[i-1] == 1:
                return i
            else:
                dups[i-1] = 1
        
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
    
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
