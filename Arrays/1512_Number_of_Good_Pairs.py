class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pair=0
        length=len(nums)
        i=0
        while i <length:
            j=i+1
            while j<length:
                if nums[i] == nums[j]:
                    pair = pair + 1
                j = j + 1
            i = i + 1



        return pair
