class Solution:
    def specialArray(self, nums: List[int]) -> int:
        i = 0 
        while i <= len(nums):
            count = 0
            #print(i, count)
            j = 0
            while j < len(nums):
                if nums[j] >= i:
                    count += 1
                j += 1
            #print(i, count)
            if count == i: return i
            i += 1
        return -1

