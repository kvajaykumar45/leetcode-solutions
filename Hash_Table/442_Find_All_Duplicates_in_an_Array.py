class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [k for k,v in Counter(nums).items() if v>1 ]
            
