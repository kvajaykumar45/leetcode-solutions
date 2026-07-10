class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1 
                nums[k] = nums[i]
                k += 1
        return k
